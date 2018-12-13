##Needs refactoring
state = '#..######..#....#####..###.##..#######.####...####.##..#....#.##.....########.#...#.####........#.#.'

# state = '#..#.#..##......###...###'

rules = open('day12_input.txt').read() 
# rules='''...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #'''

create_plant = [line[0:5] for line in rules.splitlines() if line[9] == '#']

shift = 1000
state = '.'*shift + state + '.'*shift
count = 0
total = 0
for generation in range(10000):
    new_state = state
    for i in range(2,len(state)):    
        current_set = state[i-2:i+3]
        
        if current_set in create_plant:
            new_state= new_state[:i] + "#" + new_state[i+2:]
        else:
            new_state= new_state[:i] + "." + new_state[i+2:]
    
    state = new_state
    
    prev_total = total 
    total = 0
    
    
    
    for i,pot in enumerate(state):
        if pot == '#':
            total+= i-shift
    nplants = sum(c=='#' for c in state)
    print(nplants)
    
    if nplants >=63:
        count+=1
    if count == 100:
        break
    
    print(f'{generation+1}, {total}, {total - prev_total}')
    total = prev_total

# print(state)

# print(state)

        

