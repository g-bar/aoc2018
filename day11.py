import numpy as np
import time
grid_serial_number = 8444

grid = np.zeros((300,300))

for x in range(300):
    for y in range(300):
        rackid = x+1 + 10
        powerlevel = rackid * (y+1)
        powerlevel += grid_serial_number
        powerlevel *= rackid
        powerlevel = [int(d) for d in str(powerlevel)][-3] if powerlevel >= 100 else 0
        powerlevel -= 5
        grid[x,y] = powerlevel

def get_max_power(square_size):
    max_power = 0
    coords = None

    for x in range(0,300-square_size):
        for y  in range(0,300-square_size):            
            square_power = int(np.sum(grid[x:x+square_size, y:y+square_size]))
            if square_power >= max_power:
                max_power = square_power
                coords = (x+1, y+1)
    return max_power, coords

max_power = 0

print(get_max_power(3))


t0 = time.time()
for size in range(1,301):
    print(f'{size}: cumtime:{time.time()-t0:0.3f} s')
    m, c = get_max_power(size)
    if m > max_power:
        max_power = m
        coords = c
        max_size = size

print(max_power)
print(coords, max_size)
