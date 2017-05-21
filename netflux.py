from transpiler.parser import *
from sys import argv

# Running the interpreter of netflux

filename = argv
try:
    f = open(filename[1], 'r')
except IndexError:
    print("You forgot to input the file containing your code!")
    print("Type:\tpython3 run.py <filename.txt>")

temp = ""
for line in f:
    try:
        if "end" in line:
            temp += line.rstrip()
            parser.parse(temp)
            temp = ""
        elif "if" in line or len(temp) > 0:
            temp += line.rstrip()
            continue
        else:
            parser.parse(line.rstrip())
    except EOFError:
        break
