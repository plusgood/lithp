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
		self.replace_self_with_func_names()

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
		pass

	def make_main_method(self):
		pass

	def get_cpp(self):
		"""Return converted C++ code as a string
		"""
		return self.converted
