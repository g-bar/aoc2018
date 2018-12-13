import re

theinput = open('day3_input.txt').read()

#Part 1
fabric = [[0 for i in range(1000)] for i in range(1000)]
pattern = re.compile(r"^#\d+ @ (\d+),(\d+): (\d+)x(\d+)$")
input1 = theinput.splitlines()

overlaps = 0
for claim in input1:
    left, top, width, height = map(int,pattern.match(claim).groups())
    for i in range(top, top+height):
        for j in range(left, left+width):            
            fabric[i][j] +=1
            if fabric[i][j]==2:
                overlaps+=1

#Part 2
for claim in input1:
    left, top, width, height = map(int,pattern.match(claim).groups())
    if all(all(col==1 for col in r[left:left+width]) for r in fabric[top:top+height]):
        res2 = re.search(fr'#(\d+) @ {left},{top}', theinput).group(1)
        break
print(res2)





        


            



