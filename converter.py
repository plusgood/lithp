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

		self.converted = ''

		return self.converted

	def make_func_dict(self):
		pass

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
