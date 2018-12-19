from collections import defaultdict, Counter, deque

use_example_input = False
file =  'day18_input.txt' if not use_example_input else 'day18_example.txt'
input_lines = open(file).read().splitlines()
mapping = defaultdict(str)

for y, row in enumerate(input_lines):
    for x,el in enumerate(row):
        mapping[complex(y,x)] = el



def search_adjacent(c, val, mapping):
    count = 0
    for op in -1-1j, -1, -1+1j, -1j, 1j, 1-1j, 1, 1+1j:
        if mapping[c + op] == val:
            count += 1
    return count

results = set()
loop = []
flag = False
first_pattern = None

for m in range(1, 1_000_000_000):
    new_state = mapping.copy()
    
    for number, value in mapping.copy().items():
        if value == '.':
            if search_adjacent(number, '|', mapping)>=3:
                new_state[number] = '|'
        
        elif value == '|':
            if search_adjacent(number, '#', mapping)>=3:
                new_state[number] = '#'
        elif value == '#':
            if not (search_adjacent(number, '#',mapping) >=1 and search_adjacent(number, '|', mapping) >= 1):
                new_state[number] = '.'
    
    mapping = new_state
    pattern = tuple(mapping.items())
    if flag and first_pattern == pattern:
        break
    
    if pattern in results and not flag:
        flag = True
        first_in_loop = m
        first_pattern = pattern
   
    
    results.add(tuple(mapping.items()))

    

    if flag:
        c = Counter(mapping.values())
        r = c['#'] * c["|"]
        loop.append(r)
        

idx = (1000000000 - first_in_loop) % len(loop)
print(loop[idx])