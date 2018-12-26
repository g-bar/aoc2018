from functools import reduce
from itertools import accumulate, cycle, dropwhile
from collections import defaultdict

def part1(changes):
    return sum(changes)

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
