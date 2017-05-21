import ply.yacc as yacc
from transpiler.lexer import *

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
    statement : expression DOT
              | read DOT
              | var_assign DOT
              | list_access_assign DOT
              | print_statement DOT
              | if_statement
              |
    '''
    run(p[1])

def p_blocks(p):
    '''
    blocks : block
           | blocks block
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_block(p):
    '''
    block : expression DOT
          | read DOT
          | var_assign DOT
          | list_access_assign DOT
          | print_block DOT
          | if_statement
          |
    '''
    p[0] = p[1]

def p_print_statement(p):
    '''
    print_statement : PRINT expression
                    | PRINT read
                    | PRINT STRING
    '''
    print(run(p[2]))

def p_print_block(p):
    '''
    print_block : PRINT expression
                | PRINT read
                | PRINT STRING
    '''
    p[0] = ('print', p[2])

def p_ifstatement(p):
    '''
    if_statement : IF LPAREN expression RPAREN blocks END
    '''
    if (run(p[3])):
        run(p[5])
    else:
        p[0] = None


def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression
               | NAME EQUALS STRING
               | NAME EQUALS read
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


def p_read(p):
    '''
    read : READ LPAREN CONSOLE RPAREN
         | READ LPAREN STRING RPAREN
    '''
    p[0] = ('read', p[3])


def p_eval(p):
    '''
    expression : EVAL LPAREN STRING RPAREN
               | EVAL LPAREN NAME RPAREN
               | EVAL LPAREN read RPAREN
    '''
    p[0] = ('eval', run(p[3]))


def p_write_to_file(p):
    '''
    boolean : WRITE LPAREN STRING COMMA STRING RPAREN
            | WRITE LPAREN STRING COMMA expression RPAREN
            | WRITE LPAREN STRING COMMA read RPAREN
    '''
    p[0] = ('write', run(p[3]), run(p[5]))


def p_error(p):
    return "SyntaxError"


# Create a parser

parser = yacc.yacc()
env = {}

def run(p):
    global env
    if type(p) == tuple:

        if p[0] == 'print':
            print(run(p[1]))

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
                print('NameError: Undeclared variable found!')
                quit()
            else:
                return env[p[1]]

        elif p[0] == 'access':
            try:
                return env[p[1]][p[2]]
            except IndexError:
                print('IndexError: List index out of range')
                quit()

        elif p[0] == 'access_assign':
            try:
                env[p[1]][p[2]] = p[3]
                return p[3]
            except IndexError:
                print('IndexError: List index out of range')
                quit()

        elif p[0] == 'unary':
            if p[1] == '+':
                return run(p[2])
            elif p[1] == '-':
                return -run(p[2])

        elif p[0] == 'read':
            if p[1] == 'console':
                return input()
            else:
                target = open(run(p[1]), 'r')
                output = target.read()
                target.close
                return output

        elif p[0] == 'eval':
            try:
                return eval(p[1])
            except NameError:
                print('TypeError: eval() arg must be a string of numbers')
                quit()
            except TypeError:
                print('TypeError: eval() arg must be a string object')
                quit()

        elif p[0] == 'write':
            target = open(run(p[1]), 'w')
            target.write(str(run(p[2])))
            target.close
            return True

    elif type(p) == list:
        if type(p[0]) == tuple:
            for i in p:
                run(i)
            return
        else:
            return p

    else:
        return p
