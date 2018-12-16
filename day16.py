import re
from collections import defaultdict
from collections import Counter
from itertools import dropwhile
input = open('day16_input.txt').read().splitlines()
count = 0
counter = defaultdict(Counter)

#634 too low

pat1 = re.compile(r'(\[.+\])')
pat2= re.compile(r'(\d+)')
before = []
opcode = []
after = []

for line_index, line in enumerate(input):    
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
    
def addr(before, after, input):
    code, A, B, C = input
    before[C] = before[A] + before[B]
    if before == after:
        counter[addr][code]+=1
        return True

def addi(before, after, input):
    code, A, B, C = input
    before[C] = before[A] + B
    if before == after:
        counter[addi][code]+=1
        return True

def mulr(before, after, input):
    code, A, B, C = input
    before[C] = before[A] * before[B]
    if before == after:
        counter[mulr][code]+=1
        return True

def muli(before, after, input):
    code, A, B, C = input
    before[C] = before[A] * B
    if before == after:
        counter[muli][code]+=1
        return True

def banr(before, after, input):
    code, A, B, C = input
    before[C] = before[A] & before[B]
    if before == after:
        counter[banr][code]+=1
        return True

def bani(before, after, input):
    code, A, B, C = input
    before[C] = before[A] & B
    if before == after:
        counter[bani][code]+=1
        return True

def borr(before, after, input):
    code, A, B, C = input
    before[C] = before[A] | before[B]
    if before == after:
        counter[borr][code]+=1
        return True

def bori(before, after, input):
    code, A, B, C = input
    before[C] = before[A] | B
    if before == after:
        counter[bori][code]+=1
        return True

def setr(before, after, input):
    code, A, B, C = input
    before[C] = before[A]
    if before == after:
        counter[setr][code]+=1
        return True

def seti(before, after, input):
    code, A, B, C = input
    before[C] = A
    if before == after:
        counter[seti][code]+=1
        return True

def gtir(before, after, input):
    code, A, B, C = input
    before[C] = int(A > before[B])
    if before == after:
        counter[gtir][code]+=1
        return True

def gtri(before, after, input):
    code, A, B, C = input
    before[C] = int(before[A] > B)
    if before == after:
        counter[gtri][code]+=1
        return True

def gtrr(before, after, input):
    code, A, B, C = input
    before[C] = int(before[A] > before[B])
    if before == after:
        counter[gtrr][code]+=1
        return True

def eqir(before, after, input):
    code, A, B, C = input
    before[C] = int(A == before[B])
    if before == after:
        counter[eqir][code]+=1
        return True

def eqri(before, after, input):
    code, A, B, C = input
    before[C] = int(before[A] == B)
    if before == after:
        counter[eqri][code]+=1
        return True

def eqrr(before, after, input):
    code, A, B, C = input
    
    before[C] = int(before[A] == before[B])
    if before == after:
        counter[eqrr][code]+=1
        return True

samplecounter = 0
for b, a, i in zip(before, after, opcode):
    opcounter = 0    
    for op in [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]:
        
        if op(b[:],a[:],i[:]):
            opcounter +=1
    
    if opcounter >= 3:
        samplecounter+=1

for op in counter:
    print(op.__name__, counter[op])

counters = sorted(list(counter.items()), key= lambda t: len(t[1]))

assigned = []
mapping = {}
while len(assigned)< 16:
    for op, counter in counters:
        if len(counter) == 1:
            for c in counter:
                assigned.append(c)
                mapping[c] = op

        else:
            for k in counter.copy():
                if k in assigned:
                    del counter[k]

print(i)

for _, line in dropwhile(lambda t: t[0] < line_index, enumerate(input)):
    opcode = [int(n) for n in pat2.findall(line)]
    