from functools import reduce
from itertools import accumulate, cycle, dropwhile
from collections import defaultdict


##For efficiency 
## https://en.wikipedia.org/wiki/Closest_pair_of_points_problem
#https://stackoverflow.com/questions/12232930/finding-out-the-minimum-difference-between-elements-in-an-array/25213053#25213053

def part1(changes):
    return sum(changes)


# Nice solution from 
# https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eauapmb

# seen = set{0}
# result = next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f))

# Alternatively
# resslt = next(dropwhile(lambda f: not (f in seen or seen.add(f)), accumulate(cycle(changes))))
         

def part2(changes):     
    d = defaultdict(int)
    for i,n in enumerate(accumulate(cycle(changes)),1):
        d[n]+=1
        if d[n] == 2:
            return n
if __name__ == "__main__":
    with open('day1_input.txt', 'r') as theinput:
        theinput = theinput.read()

    changes = [int(n) for n in theinput.split()]

    r_part1 = part1(changes)
    r_part2 = part2(changes)

    print(r_part1)
    print(r_part2)
