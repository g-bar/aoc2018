import re
from collections import defaultdict
from collections import Counter
from itertools import dropwhile
inplines = open('day16_input.txt').read().splitlines()
count = 0
counter = defaultdict(Counter)

pat1 = re.compile(r'(\[.+\])')
pat2= re.compile(r'(\d+)')
before = []
opcode = []
after = []

for line_index, line in enumerate(inplines):    
    if line == '':
        count+=1
        if count == 3:
            line_index+=1
            break
        continue
    count = 0

    if 'Before' in line:
            before.append(eval(pat1.findall(line)[0]))
    elif 'After'in line:
            after.append(eval(pat1.findall(line)[0]))
    else: 
        opcode.append([int(n) for n in pat2.findall(line)])
    
def addr(register, input):
    A, B, C = input
    register[C] = register[A] + register[B]
    return register

def addi(register, input):
    A, B, C = input
    register[C] = register[A] + B
    return register

def mulr(register, input):
    A, B, C = input
    register[C] = register[A] * register[B]
    return register

def muli(register, input):
    A, B, C = input
    register[C] = register[A] * B
    return register

def banr(register,input):
    A, B, C = input
    register[C] = register[A] & register[B]
    return register

def bani(register, input):
    A, B, C = input
    register[C] = register[A] & B
    return register

def borr(register, input):
    A, B, C = input
    register[C] = register[A] | register[B]
    return register

def bori(register, input):
    A, B, C = input
    register[C] = register[A] | B
    return register

def setr(register, input):
    A, B, C = input
    register[C] = register[A]
    return register

def seti(register, input):
    A, B, C = input
    register[C] = A
    return register

def gtir(register, input):
    A, B, C = input
    register[C] = int(A > register[B])
    return register

def gtri(register, input):
    A, B, C = input
    register[C] = int(register[A] > B)
    return register

def gtrr(register, input):
    A, B, C = input
    register[C] = int(register[A] > register[B])
    return register

def eqir(register, input):
    A, B, C = input
    register[C] = int(A == register[B])
    return register

def eqri(register, input):
    A, B, C = input
    register[C] = int(register[A] == B)
    return register

def eqrr(register, input):
    A, B, C = input
    register[C] = int(register[A] == register[B])
    return register

samplecounter = 0

for b, a, i in zip(before, after, opcode):
    opcounter = 0    
    for op in [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]:
        r = b[:]
        code, *input = i
        if op(r, input) == a:
            opcounter +=1
            counter[op][i[0]] +=1
    
    if opcounter >= 3:
        samplecounter+=1

print(samplecounter)

counters = sorted(list(counter.items()), key= lambda t: len(t[1]))

assigned = []
mapping = {}
while len(assigned)< 16:
    for op, counter in counters[:]:
        if len(counter) == 1:
            for c in counter:
                assigned.append(c)
                mapping[c] = op
                counters.remove((op,counter))

        else:
            for k in counter.copy():
                if k in assigned:
                    del counter[k]

r = [0,0,0,0]


for _, line in dropwhile(lambda t: t[0] < line_index, enumerate(inplines)):    
    opid, *in_ = [int(n) for n in pat2.findall(line)]
    mapping[opid](r,in_)

print(r)