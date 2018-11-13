import scanner
import token
import parser

print("--------------------------------------")
print("| Welcome to DB Stimulation Program! |")
print("--------------------------------------")
print("\n\n\n\n")
print("Enter SQL Statements:")
Parser = parser.parser()
code = ""
single_quote_flag = False
double_quote_flag = False
while True:

	input_string = input(">> ")
	for ch in input_string:
		if single_quote_flag and ch == "'":
			single_quote_flag = False
			code += ch
		elif single_quote_flag:
			code += ch
		elif double_quote_flag and ch =='"':
			double_quote_flag = False
			code += ch
		elif double_quote_flag:
			cpde += ch
		elif ch == "'":
			single_quote_flag = True
			code += ch
		elif ch == '"':
			double_quote_flag = True
			code += ch
		elif code == ';':
			code += ch
			Parser.parse(code)
			code = ""
		else:
			code += ch 

