import re
from lexer import Lexer

class Converter(object):
	"""Takes a string that represents a raw
	Lithp program, and converts it to C++.
	"""

	TYPES_DICT = { #only types that change names when converted to C++
		'int' : 'long long',
	}

	FUNCS_DICT = { #only functions that change names when converted to C++
		#These three can't be used as macros
		'or' : 'or_',
		'and' : 'and_',
		'not' : 'not_'
	}

	def __init__(self, program):
		self.program = program
		self.lexer = Lexer(self.program)
		self.tokens = self.lexer.get_tokens()


		#Initializations (some are pointless (self.main, self.converted))
		self.func_count = 0
		self.func_dict = {} #{func_name: func_header_and_body, ...}
		self.cpp_declarations = {} #{func_name : cpp_func_decl, ...}
		self.func_bodies = {} #{func_name: func_body, ...}
		self.cpp_func_bodies = {} #{func_name: cpp_func_body, ...}
		self.main = ''
		self.cpp_main = ''

		self.converted = ''

		self.convert() #sets self.converted

	def convert(self):
		"""Converts the program into C++ code
		Code must be compiled wth lithp.hpp
		"""
		self.make_func_dict() #sets self.func_dict
		self.make_main_function() #sets self.main
		self.remove_lambda_nesting()
		self.replace_self_with_func_names()
		self.make_func_declarations() #sets self.cpp_declarations
		self.make_func_bodies() #sets self.cpp_func_bodies		
		self.make_cpp_func_bodies()

		return self.converted

	def make_func_dict(self):
		"""Looks at tokens and forms dictionary
		mapping generated function names to function
		bodies
		"""
		index = 0
		while index < len(self.tokens):
			if self.tokens[index] == '\\': #Lambda
				#Every lambda looks like this:
				#(\ (param1:type1, ...) : return_type
				#  expression)

				#That expression can then be used as a function
				#i.e. (  (\(...):type (...))  param1 param2 ...)
				#     calls the lambda

				#Parentheses around entire function
				i = self.tokens.match_paren(index - 1)

				#Create unique function name
				func_name = 'f%d' % self.func_count

				#                           function body
				self.func_dict[func_name] = self.tokens[index-1:i+1].get_joined()
				self.func_count += 1

			index += 1

		return self.func_dict

	def remove_lambda_nesting(self):
		"""
		Removes any anonymous functions that are nested inside
		other anonymous functions and replaces them with their
		generated function names

		Precondition: make_func_dict must have been called
		"""

		#Iterate through each pair of functions
		#if one is present in another, replace its body with its name
		for f in self.func_dict:
			for g in self.func_dict:
				if f == g: continue #Don't want to replace a function with itself!
				self.func_dict[f] = self.func_dict[f].replace(self.func_dict[g], g)

		return self.func_dict

	def replace_self_with_func_names(self):
		"""Replaces the context dependent Lithp
		keyword `self` with the generated name
		of the function in the C++ code
		
		Precondition: make_func_dict must have been called
		"""
		for name in self.func_dict:
			self.func_dict[name] = self.func_dict[name].replace('self', name)

	def make_func_declarations(self):
		"""Creates function declarations with parameter
		types and return types. Higher order functions
		are supported. Function declarations are also
		used as function signatures.

		Precondition: make_func_dict must have been called
		"""

		for name in self.func_dict:
			body = Lexer(self.func_dict[name]).get_tokens()
			i = body.index('\\')  + 1 #Start of parameters
			j = body.match_paren(i)
			param_tokens = body[i + 1: j] #Stuff inside parentheses
			#			print "param list:", param_tokens

			params = self.split_params(param_tokens)
			params = map(lambda n: n.split(':'), params)
			#params is now [[<name>,<type>],...]
			c_types = map(lambda n: self.convert_type(*n), params)
			#			print c_types

			return_type = ''
			#     +2 to skip over ")" and ":"
			if body[j+2] == '(': #Function returns another function
				#                                  +3 for [")","->","<type>"]
				for x in xrange(j+2, body.match_paren(j+2)+3):
					return_type += body[x]
			else: #Function returns a concrete type
				return_type = body[j+2] #+2 to skip over ")" and ":"

			func_type = self.convert_type(name, return_type)
			#			print "params", params
			#			print "c_types", c_types
			#while True:exec raw_input() in globals(), locals()
			self.cpp_declarations[name] = func_type + '(' + ', '.join(c_types) + ')'

		self.cpp_declarations['main'] = 'int main()'

	def split_params(self, params):
		"""Takes params without surrounding parentheses
		and splits them into a list. `params` is a Tokens
		object
		"""
		index = 0
		acc = ''
		ret = [] #return value (is ret a bad name?)
		while index < len(params):
			if params[index] == ',': #End of a parameter
				ret.append(acc)
				acc = ''
			elif params[index] == '(': #start of a type that is a function
				end = params.match_paren(index)
				while index <= end: #so the commas in the function type
					#                are disregarded
					acc += params[index]
					index += 1
				continue #so index doesn't get incremented again
			else:
				acc += params[index]
			index += 1

		if acc: #if they ended the list with a comma then acc would be ''
			ret.append(acc) #parameters not ended with a comma,
			#                acc last the last param

		return ret

	def convert_type(self, name, type):
		"""Converts a string that is a name and a
		string that constitutes a type that may
		be simple (e.g. int, double) or a function 
		(e.g. (int,int)->int) into its C++ definition.
		`name` may be an empty string.
		convert_type('x', 'int') => 'int x'
		convert_type('x', '(int,double)->bool') => bool (*x)(int,double)
		"""
		#		print 'Called with name = %s and type = %s' %(name, type)
		name = ''.join(name.split())
		type = ''.join(type.split())

		if re.match(r'\w+', type): #It's a concrete type
			return self.TYPES_DICT.get(type,type) + ' ' + name

		arrow = type.rfind('->')
		assert arrow != -1, "If it's not a primitive, it must be a function"
		params, return_type = type[:arrow], type[arrow+2:]
		assert params[0] == '(' and params[-1] == ')'
		params = params[1:-1]

		params_tokenized = Lexer(params).get_tokens()
		param_list = self.split_params(params_tokenized)
		cpp_params = map(lambda n: self.convert_type('', n), param_list)
		return_type = self.convert_type('', return_type)
		return return_type + ' (*' + name + ')(' + ', '.join(cpp_params) + ')'


	def make_func_bodies(self):
		"""Extracts bodies of lambda functions
		(as opposed to their headers). These bodies
		will then be translated to a series of function
		calls.
		"""
		for name in self.func_dict:
			tok = Lexer(self.func_dict[name]).get_tokens()
			end = tok.match_paren(0)
			header_end = tok.match_paren(2)

			if tok[header_end+2] == '(': #Function returns another function
				start = body.match_paren(header_end+2)+3
			else: #Function returns a concrete type
				start = header_end+3
			
			self.func_bodies[name] = tok[start:end].get_joined()

		self.func_bodies['main'] = self.main


	def make_main_function(self):
		"""Finds the outermost function call
		which will go in the main method
		This adds the function int main() to func_dict
		and func_declarations.
		"""
		self.main = self.tokens.get_joined()
		for func in self.func_dict:
			self.main = self.main.replace(self.func_dict[func], func)

	def make_cpp_func_bodies(self):
		"""Use the extracted Lithp function bodies
		and convert them to C style function calls.
		i.e. (f a b) => f(a,b)
		"""
		for name, body in self.func_bodies.iteritems():
			t = Lexer(body).get_tokens()			
			S = [] #Stack
			x = 0
			while x < len(t):
				if t[x] == '(': #function call begins
					x += 1
					S.append(self.FUNCS_DICT.get(t[x], t[x]) + '(')
				elif t[x] == ')': #function call ends
					acc = ''
					while S[-1][-1] != '(':
						#pop off params until function call is reached
						acc = S.pop() + ',' + acc
					# [:-1] to strip off comma at the end
					S.append(S.pop() + acc[:-1] + ')') #S.pop() gives function
				else:
					S.append(t[x])
				x += 1
			self.cpp_func_bodies[name] =  S[0]

	def get_cpp(self):
		"""Return converted C++ code as a string
		"""
		return self.converted
