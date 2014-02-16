import re


class Lexer(object):
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
		self.rejoin_tokens() #Sets self.joined

	def match_paren(self, index):
		"""Matches parenthesis at `index`,
		returns index of matching parenthesis
		"""
		
		assert self.tokens[index] == '(', \
			   "Supplied index must point to a parenthesis"
		
		c = 1 #Counter for parentheses depth
		while c != 0:
			if c < 0:
				raise LexingError, "Unbalanced parentheses"
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
		self.joined = ' '.join(self.tokens)
		return self.joined

	def get_joined(self):
		"""Returns tokens joined back together
		into a string
		"""
		return self.joined

	def __len__(self):
		return len(self.tokens)

	def __getitem__(self, index):
		result = self.tokens[index]
		if hasattr(result, '__iter__'): #If they wanted a slice
			return Tokens(result) #result is a sublist (a slice)
		else:
			return result #This is just a string

	def __iter__(self):
		for x in self.tokens:
			yield x
		


class LexingError(Exception):
	pass

	
