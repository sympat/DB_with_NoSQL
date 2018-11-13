import token
import scanner

class parser:
	Scanner = scanner.scanner()
	result = []
	def __init__(self):
		return

	def accept(expected_token_kind):
		if self.current_token.kind == expected_token_kind:
			self.result.append(self.current_token)
			self.current_token = self.Scanner.get_next_token()
			

	def parse(self, source):
		self.Scanner.set_source(source)
		self.current_token = self.Scanner.get_next_token()
		if current_token.kind == Token.CREATE:
			self.parseCreatestmt()


	def parseCreatestmt(self):
		self.accept(Token.CREATE)