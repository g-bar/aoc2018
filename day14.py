input = '846021'

from collections import deque 

length = len(str(input))
scores = [3,7]
nrecipes = 2
elves = [0,1]

cond1 = [int(n) for n in str(input)] != scores[-length:]
cond2 = [int(n) for n in str(input)] != scores[-length-1:-1]

while cond1 and cond2  :
    new = [int(n) for n in str(scores[elves[0]] + scores[elves[1]])]
    nrecipes += len(new)
    scores.extend(new)    
    for i, elf in enumerate(elves):
        elves[i] += scores[elf] + 1
        elves[i] %= len(scores)

    cond1 = [int(n) for n in str(input)] != scores[-length:]
    cond2 = [int(n) for n in str(input)] != scores[-length-1:-1]
    
    print(nrecipes)

if not cond1:
    print(len(scores[:-length]))
elif not cond2:
    print(len(scores[:-length-1]))

