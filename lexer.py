import ply.lex as lex

# Tokens for netflux
tokens = [
    'INT',
    'REAL',
    'STRING',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'MODULUS',
    'EQUALS'
]

# Setting up tokens
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_POWER = r'\*\*'
t_MULTIPLY = r'\*'
t_MODULUS = r'\%'
t_EQUALS = r'\='

# Ignore white-space tokens
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

def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal characters!")
    t.lexer.skip(1)


# Create a lexer
lexer = lex.lex()
