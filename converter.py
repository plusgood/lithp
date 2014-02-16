import re
from parser import Parser

class Converter(object):
	"""Takes a string that represents a raw
	Lithp program, and converts it to C++.
	"""

	def __init__(self, program):
		self.program = program
		self.parser = Parser(program)
		self.tokens = self.parser.get_tokens()
		self.convert() #sets self.converted

	def convert(self):
		"""Converts the program into C++ code
		Code must be compiled wth lithp.hpp
		"""
		self.make_func_dict() #sets self.func_dict
		
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
				#i.e. (  (\(...):type (...))  param1 param2 ...) Calls the lambda

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
		pass

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
