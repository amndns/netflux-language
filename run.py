from parser import *
from sys import argv

# Running the interpreter of netflux
f = open('sample.txt', 'r')

for line in f:
    try:
        s = line.rstrip()
    except EOFError:
        break
    parser.parse(s)
