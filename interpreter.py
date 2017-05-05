from transpiler.parser import *

# Running the interpreter of netflux

while True:
    try:
        s = input('>> ')
    except EOFError:
        break
    parser.parse(s)
