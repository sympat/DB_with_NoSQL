import token

space_char = {' ', '\t', '\n', '\r'}

def isDigit(x):
	return '0' <= x <= '9'

def isAlpha(x):
	return ('a' <= x <= 'z') || ('A' <= x <= 'Z')


class scanner:
	source = None
	cur_token = ""
	cur_char = " "
	cur_kind = None
	def __init__(self):
		
	def set_source(self, source):
		self.source = source
		self.get_next_char()
	def get_next_char(self):
		if self.source == "":
			self.cur_char = "$"
			return
		self.cur_char = self.source[0]
		self.source = self.source[1:]

	def push_char(self):
		self.cur_token.append(self.cur_char)
		self.get_next_char()

	def send_cur_token(self):
		ret = token.token(self.cur_kind, self.cur_token)
		self.cur_token = ""
		return ret

	def get_next_token(self):
		while self.cur_char in space_char :
			self.get_next_char()
		self.cur_kind = self.scan()
		self.send_cur_token()

	def scan(self):
		if self.cur_char == "$":
			self.push_char()
			return token.EOF
		if self.cur_char == "+":
			self.push_char()
			return token.PLUS
		if self.cur_char == "-":
			self.push_char()
			return token.MINUS
		if self.cur_char == ">":
			self.push_char()
			if self.cur_char == "=":
				self.push_char()
				return token.GREATEREQ
			return token.GREATER
		if self.cur_char == "<":
			self.push_char()
			if self.cur_char == "=":
				self.push_char()
				return token.LESSEQ
			return token.LESS
		if self.cur_char == "=":
			self.push_char()
			if self.cur_char == "=":
				self.push_char()
				return token.EQ
			return token.ASSIGN
		if self.cur_char == "{":
			self.push_char()
			return token.LEFTBRACE
		if self.cur_char == "}":
			self.push_char()
			return token.RIGHTBRACE
		if self.cur_char == "(":
			self.push_char()
			return token.LEFTPAREN
		if self.cur_char == ")":
			self.push_char()
			return token.RIGHTPAREN
		if isDigit(self.cur_char):
			while isDigit(self.cur_char):
				self.push_char()
			if self.cur_char == ".":
				self.push_char()
				while isDigit(self.cur_char):
					self.push_char()
				return token.FLOATLITERAL
			return token.INTLITERAL
		if isAlpha(self.cur_char):
			while isDigit(self.cur_char) or isAlpha(self.cur_char):
				self.push_char()
			if cur_token in token.keywords:
				
		
		
