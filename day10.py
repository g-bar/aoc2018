import re
import numpy as np
inpstr = open('day10_input.txt').read()
inplines = inpstr.splitlines()

pat = re.compile(r'-?\d+')
positions = []
velocities = []

for lines in map(pat.findall, inplines):
    x, y, vx, vy = list(map(int, lines))
    positions.append((x,y))
    velocities.append((vx,vy))

pos = np.array(positions) 
vels = np.array(velocities)

##FAILED SEE REDDIT SOLUTIONS
area = float('inf')
for i in range(1000000):
    pos += vels
    
    min_ = pos.min(axis=0)
    max_ = pos.max(axis=0)
    print(max_,min_)
    len = max_ - min_
    print(len)
    iarea = len[0] * len[1]

    area = min(area, iarea)
    print(area)