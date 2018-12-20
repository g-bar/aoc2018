import re
from day16 import *
import __main__
import time

#6
use_example_input = False
file = 'day19_input.txt' if not use_example_input else 'day19_example.txt'

inputstr = open(file).read()

find_instr = re.compile('[a-z]+')
find_nums = re.compile(r'\d+')


instructions = []
for line in inputstr.splitlines():
    if '#ip' in line:
        bound_register = int(find_nums.findall(line).pop())
    else:
        instr = find_instr.findall(line).pop()
        inps = [int(n) for n in find_nums.findall(line)]

        instructions.append((instr, inps))


r = [0,0,0,0,0,0]

pointer = r[bound_register]
n = 0
while True:
    if r[5] == 861:
        breakpoint()
    try:
        funcname, inps  = instructions[pointer]
    except IndexError:
        break
    n+=1
    r[bound_register] = pointer
    getattr(__main__, funcname)(r, inps)
    print(f'{n}: {r}' + ' '*80, end='\r')
    pointer = r[bound_register]
    pointer += 1
    
print(r[0])
