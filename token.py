class token:
	kind = None
	content = None
	def __init__(self, kind, content):
		self.kind = kind
		self.content = content

ID			, 		# identifier
BITOR		,		# |
BITAND		,		# &
BITXOR		,		# ^
EQ			,		# =
NOTEQ		,		# <>
LESSEQ		,		# <=
LESS		,		# <
GREATER		,		# >
GREATEREQ	,		# >=
PLUS		,		# +
MINUS		,		# -
TIMES		,		# *
DIV			,		# /
MOD			,		# %
INTLITERAL	,
FLOATLITERAL,
STRINGLITERAL,

# keywords:
ALL			,
AND			,
ANY			,
BETWEEN		,
EXISTS		,
IN			,
LIKE		,
NOT			,
OR			,
SOME		,
CREATE		,
TABLE		,
DROP		,
FROM		,
INSERT		,
SELECT		,
SHOW		,
UPDATE		,
WHERE		,

# punctuation:
LEFTBRACE 	,	# {
RIGHTBRACE	,	# }
LEFTBRACKET	,	# [
RIGHTBRACKET,	# ]
LEFTPAREN	,	# (
RIGHTPAREN	,	# )
COMMA		,	# ,
SEMICOLON	,	# ;

# special tokens:
ERROR		,
EOF			= range(47)   # end-of-file

keywords = {"ALL" : ALL,
			"AND" : AND,
			"ANY" : ANY,
			"BETWEEN" : BETWEEN,
			"EXISTS" : EXISTS,
			"IN" : IN,
			"LIKE" : LIKE,
			"NOT" : NOT,
			"OR" : OR,
			"SOME" : SOME,
			"CREATE" : CREATE,
			"TABLE" : TABLE,
			"DROP" : DROP,
			"FROM" : FROM,
			"INSERT" : INSERT,
			"SELECT" : SELECT,
			"SHOW" : SHOW,
			"UPDATE" : UPDATE,
			"WHERE" : WHERE}