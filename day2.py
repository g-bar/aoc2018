from collections import Counter
from itertools import combinations, compress

theinput = open('day2_input.txt').read().split()

#Part1

count2 = [1 for c in (Counter(id) for id in theinput) if 2 in c.values()]
count3 = [1 for c in (Counter(id) for id in theinput) if 3 in c.values()]
res1 = sum(count2) * sum(count3)
print(res1)

#Part2

for one, two in combinations(theinput, 2):    
    diff = [e1 == e2 for e1,e2 in zip(one,two)]    
    if sum(diff) == (len(one) - 1):
        res2 = ''.join(compress(one,diff))
        break

print(res2)
