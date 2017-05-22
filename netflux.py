from transpiler.parser import *
from sys import argv

# Running the interpreter of netflux

filename = argv
try:
    f = open(filename[1], 'r')
except IndexError:
    print("You forgot to input the file containing your code!")
    print("Type:\tpython3 run.py <filename.txt>")

string = ""
for line in f:
    try:
        string += line.rstrip()
        string += " "
    except EOFError:
        break
parser.parse(string)
