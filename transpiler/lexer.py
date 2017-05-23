import ply.lex as lex


# Reserved words for netflux
reserved = {
    'length': 'LEN',

    'while': 'WHILE',
    'stop': 'STOP',

    'if' : 'IF',
    'else' : 'ELSE',
    'end': 'END',

    'write': 'WRITE',
    'read': 'READ',

    'eval': 'EVAL',
    'console': 'CONSOLE',
    'print': 'PRINT',

    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

# Tokens for netflux
tokens = [
    'INT',
    'REAL',
    'STRING',
    'NAME',

    'TRUE',
    'FALSE',

    'DOT',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'COMMA',

    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'MODULUS',
    'EQUALS',

    'EQ',
    'NEQ',
    'GT',
    'GTE',
    'LT',
    'LTE',
] + list(reserved.values())

# Setting up tokens
t_DOT = r'\.'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_POWER = r'\*\*'
t_MULTIPLY = r'\*'
t_MODULUS = r'\%'
t_EQUALS = r'\='
t_EQ = r'\=\='
t_NEQ = r'\!\='
t_GT = r'\>'
t_GTE = r'\>\='
t_LT = r'\<'
t_LTE = r'\<\='

# Ignore white-space tokens and comments
t_ignore_COMMENTS = r'//.+//'
t_ignore = r' '

# Data Types for netflux
def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TRUE(t):
    'true'
    t.value = True
    return t

def t_FALSE(t):
    'false'
    t.value = False
    return t

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, t.type)
    return t

def t_STRING(t):
    r'"(?:\\"|.)*?"'
    t.value = bytes(t.value.lstrip('"').rstrip('"'), "utf-8").decode("unicode_escape")
    return t

def t_error(t):
    print("SyntaxError: Illegal characters in '%s' found!" % t.value)
    t.lexer.skip(1)

# Create a lexer
lexer = lex.lex()
