import re
from collections import namedtuple
from functools import reduce
from operator import sub
from itertools import combinations, product

file = '25in'

findnums = re.compile(r'-?\d+')
Point = namedtuple('Point',('a,b,c,d'))

def manhattan(self, other):
    return sum(abs(a-b) for a,b in zip(self,other))

Point.manhattan = manhattan

points = sorted(Point(*map(int,nums)) for nums in (findnums.findall(line) for line in open(file)) if nums)

constellations = [set([point]) for point in points]
length = 0

while len(constellations) != length:    
    new_const = [constellations[0]]
    for c1 in constellations[1:]:
        for c2 in new_const:
            for p1, p2 in product(c1,c2):
                if p1 == p2:
                    continue
                if p1.manhattan(p2) <= 3:
                    c2.update(c1)
                    break
            else:
                continue
            break
        else:
            new_const.append(c1)
    
    constellations, length = new_const, len(constellations)

print(len(constellations))