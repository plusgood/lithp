import re
from lexer import Lexer

class Converter(object):
	"""Takes a string that represents a raw
	Lithp program, and converts it to C++.
	"""

	def __init__(self, program):
		self.program = program
		self.lexer = Lexer(program)
		self.tokens = self.lexer.get_tokens()
		self.convert() #sets self.converted

	def convert(self):
		"""Converts the program into C++ code
		Code must be compiled wth lithp.hpp
		"""
		self.make_func_dict() #sets self.func_dict
		self.remove_lambda_nesting() #sets self.no_nest
		self.converted = ''

		return self.converted

	def make_func_dict(self):
		"""Looks at tokens and forms dictionary
		mapping generated function names to function
		bodies
		"""
		index = 0
		self.func_count = 0
		self.func_dict = {}
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
				func_name = 'f%d' % func_count

				#                           function body
				self.func_dict[func_name] = self.tokens[x-1:i+1].get_joined()
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
		#A list like [[name1, body1], [name2, body2], ...]
		self.no_nest = map(list, self.func_dict.items()) #lists so it can be mutable

		#Sort by number of nested lambdas in function body
		self.no_nest.sort(key = lambda n: n[1].count('\\'))

		#Iterate through each pair of functions
		#if one is present in another, replace its body with its name
		for f in xrange(len(no_nest)):
			for g in xrange(f + 1, len(no_nest)):
				self.no_nest[g][1] = self.no_nest[g][1].replace(no_nest[f][1],
																no_nest[f][0])

		self.no_nest = dict(no_nest) #Convert n x 2 list back into dictionary

		return self.no_nest


	def make_func_declarations(self):
		pass

	def make_main_method(self):
		pass

	def replace_self_with_func_names(self):
		pass

	def get_cpp(self):
		"""Return converted C++ code as a string
		"""
		return self.converted
