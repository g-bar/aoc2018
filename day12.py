##Part one only

INPUT = 'day12_input.txt'
inputstr= open(INPUT).read()
lines = inputstr.splitlines()
state = lines[0]

spawn_plant = [line[0:5] for line in lines[1:] if line[9] == '#']
offset = 0

for generation in range(20):
    state = '....' + state + '....'    
    new_state = state
    offset+=4
    for i in range(2,len(state)-2):    
        current_set = state[i-2:i+3]
        if current_set in spawn_plant:
            new_state= new_state[:i] + "#" + new_state[i+1:]
        else:
            new_state= new_state[:i] + "." + new_state[i+1:]
    state = new_state

def compute_total(state, offset):
    total = 0
    for i,pot in enumerate(state):
        if pot == '#':
            total+= i-offset
    return total
print(compute_total(state, offset))