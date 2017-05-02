import ply.yacc as yacc
from compiler.lexer import *

# Set the precedence
precedence = (
    ('left', 'NOT', 'EQ', 'NEQ', 'GT', 'GTE', 'LT', 'LTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'POWER', 'MODULUS'),
    ('right', 'UMINUS'),
    ('right', 'UPLUS')
)

# Set of grammars in netflux

def p_statement(p):
    '''
    statement : expression
              | PRINT expression
              | var_assign
              | list_access_assign
              |
    '''
    try:
        if (p[1] == 'print'):
            print(run(p[2]))
        else:
            run(p[1])
    except IndexError:
        print("SyntaxError: invalid or empty syntax")


def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
               | NAME EQUALS STRING
    '''
    p[0] = ('=', p[1], p[3])


def p_expression(p):
    '''
    expression : expression POWER expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
               | expression MODULUS expression
               | expression PLUS expression
               | expression MINUS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float(p):
    '''
    expression : INT
               | REAL
               | boolean
    '''
    p[0] = p[1]


def p_boolean(p):
    '''
    boolean : TRUE
            | FALSE
    '''
    p[0] = p[1]


def p_boolean_operators(p):
    '''
    boolean : expression EQ expression
            | expression NEQ expression
            | expression GT expression
            | expression GTE expression
            | expression LT expression
            | expression LTE expression
            | expression AND expression
            | expression OR expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_unary_boolean_operators(p):
    '''
    boolean : NOT expression
    '''
    p[0] = (p[1], p[2])

def p_unary_operators(p):
    '''
    expression : MINUS expression %prec UMINUS
               | PLUS expression %prec UPLUS
    '''
    p[0] = ('unary', p[1], run(p[2]))


def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])


def p_comma_separated_expr(p):
    '''
    arguments : arguments COMMA expression
              | arguments COMMA STRING
              | expression
              | STRING
              |
    '''
    if len(p) == 2:
        p[0] = [run(p[1])]
    elif len(p) == 1:
        p[0] = []
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_list(p):
    '''
    expression : LBRACK arguments RBRACK
    '''
    p[0] = p[2]


def p_list_access(p):
    '''
    expression : NAME LBRACK expression RBRACK
    '''
    p[0] = ('access', p[1], run(p[3]))


def p_list_access_assign(p):
    '''
    list_access_assign : NAME LBRACK expression RBRACK EQUALS expression
                       | NAME LBRACK expression RBRACK EQUALS STRING
    '''
    p[0] = ('access_assign', p[1], run(p[3]), run(p[6]))


def p_error(p):
    return "SyntaxError"


# Create a parser

parser = yacc.yacc()
env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '%':
            return run(p[1]) % run(p[2])
        elif p[0] == '**':
            return run(p[1]) ** run(p[2])
        elif p[0] == '==':
            return run(p[1]) == run(p[2])
        elif p[0] == '!=':
            return run(p[1]) != run(p[2])
        elif p[0] == '>':
            return run(p[1]) > run(p[2])
        elif p[0] == '>=':
            return run(p[1]) >= run(p[2])
        elif p[0] == '<':
            return run(p[1]) < run(p[2])
        elif p[0] == '<=':
            return run(p[1]) <= run(p[2])
        elif p[0] == 'and':
            return run(p[1]) and run(p[2])
        elif p[0] == 'or':
            return run(p[1]) or run(p[2])
        elif p[0] == 'not':
            return not run(p[1])
        elif p[0]== '=':
            env[p[1]] = run(p[2])
            return env
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
        elif p[0] == 'access':
            try:
                return env[p[1]][p[2]]
            except IndexError:
                return 'List index out of range'
        elif p[0] == 'access_assign':
            try:
                env[p[1]][p[2]] = p[3]
                return p[3]
            except IndexError:
                return 'List index out of range'
        elif p[0] == 'unary':
            if p[1] == '+':
                return run(p[2])
            elif p[1] == '-':
                return -run(p[2])
    else:
        return p
