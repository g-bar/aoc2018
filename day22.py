from collections import defaultdict
import heapq
import numpy as np
from dataclasses import dataclass

use_example = False

depth = 4845 if not use_example else 510
tx, ty = (6, 770) if not use_example else (10,10)

limit_x = 10
limit_y = 2

themap = np.zeros((tx*limit_x, ty*limit_y))

for x in range(tx*limit_x):
    for y in range(ty*limit_y):
        if (x == 0 and y == 0) or (x==tx and y == ty):
            geologic_index = 0
        elif y == 0:
            geologic_index = x * 16807
        elif x == 0:
            geologic_index = y * 48271
        else:
            geologic_index = themap[x-1,y] * themap[x, y-1]
        
        themap[x,y] = (geologic_index + depth)%20183
        
#Part 1
print(np.sum((themap%3)[:tx+1,:ty+1]))

#Part 2
m , enabled_tools = themap%3, defaultdict(set)
tool_map = {0:('climb', 'torch'), 1: ('climb', 'neither'), 2: ('torch', 'neither')}
target = (tx, ty)

for x, row in enumerate(m):
    for y, el in enumerate(row):
        enabled_tools[(x,y)].update(tool_map[int(el)])

@dataclass(frozen = True, order=True)
class Cell():
    x: int
    y: int
    tool: str
    

start = Cell(x=0,y=0, tool = 'torch')
paths = [(0,start)]
shortest_time = defaultdict(lambda: float('Inf'))
shortest_time[start] = 0
OPS = ((0,-1), (-1,0), (1,0), (0,1))

i = 0

while paths:      
    i+=1
    print(i)
       
    t, origin = heapq.heappop(paths)            
    
    if t > shortest_time[origin]:
        continue
    best_time = shortest_time[origin]
    
    for dx,dy in OPS:                
        
        nx, ny = origin.x + dx, origin.y + dy
        new_time = best_time
        tool = origin.tool
        new_tools = enabled_tools[(origin.x, origin.y)] & enabled_tools[(nx,ny)]
        
        if not new_tools:
            continue

        if tool not in new_tools:
            new_time+=7
            tool = new_tools.pop()
        
        if (nx,ny) == target and tool != 'torch':
            new_time+=7
            tool = 'torch'
        
        new_time+=1
        new_el = Cell(x=nx,y=ny, tool=tool)

        if new_time >= shortest_time[new_el]:
            continue
        
        shortest_time[new_el] = new_time

        heapq.heappush(paths, (new_time, new_el))

print(shortest_time[Cell(x=target[0], y=target[1], tool='torch')])
