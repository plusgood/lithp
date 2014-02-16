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

	def get_cpp(self):
		"""Return converted C++ code as a string
		"""
		return self.converted
