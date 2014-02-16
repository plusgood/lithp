import re


class Parser(object):
	"""Takes a string and preprocesses and tokenizes it
	"""

	DELIMITERS = ['(', ')', ':', '\\', '->', ',']

	def __init__(self, program):
		"""Takes a string that is the raw program
		"""
		self.program = program
		self.preprocess()
		self.tokenize() #Sets self.tokens

	def preprocess(self):
		"""Preprocesses string by removing comments
		"""
		#Comments start with # and go to the end of the line
		self.program = re.sub('#.*\n', '\n', self.program)

	def tokenize(self):
		"""Tokenizes string by splitting by various delimiters:
		whitespace, parentheses, colon, backslash, ->, and comma
		All these delimiters are saved, except for whitespace
		"""

		#Split by delimiters
		delims = map(re.escape, self.DELIMITERS)
		#Parentheses surrounding entire regex mean save the delimiters
		delim_re = '(\\s+|' + '|'.join(delims) + ')'
		token_list = re.split(delim_re, self.program)

		#Removes strings that are empty or contain only whitespace
		token_list = filter(str.strip, token_list)
		
		self.tokens = Tokens(token_list)
		return self.tokens

	def get_tokens(self):
		"""Returns token list (a `Tokens` object)
		so `tokenize` doesn't have to be called again
		"""
		return self.tokens


class Tokens(object):
	"""
	Wrapper around list of tokens, providing uesful operations
	"""

	def __init__(self, tokens):
		"""
		Takes a list of strings that are tokens
		"""
		self.tokens = tokens

	def match_paren(self, index):
		"""Matches parenthesis at `index`,
		returns index of matching parenthesis
		"""
		
		assert self.tokens[index] == '(', \
			   "Supplied index must point to a parenthesis"
		
		c = 1 #Counter for parentheses depth
		while c != 0:
			if c < 0:
				raise ParsingError, "Unbalanced parentheses"
			index += 1
			if tokens[index] == ')':
				c -= 1
			elif tokens[index] == '(':
				c += 1


		#The number of close parens now equals the number of open parens
		return index

	def rejoin_tokens(self):
		"""
		Rejoins token list into a string
		"""

		#Implmentation could change to avoid unnecessary spaces between
		#parentheses etc.
		return ' '.join(self.tokens)
		


class ParsingError(Exception):
	pass

	