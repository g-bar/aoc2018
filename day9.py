#477 players; last marble is worth 70851 points
from collections import deque
from itertools import cycle

nplayers = 477
last_marble_worth = 70851 * 100

circle = deque([0])
scores = [0]* nplayers

for marble, player in zip(range(1,last_marble_worth+1), cycle([*range(1,nplayers),0])):    
    if marble % 23 :
        idx = 2%len(circle)
        circle.insert(idx, marble)
        circle.rotate(-idx)
    else:
        circle.rotate(7)
        scores[player] += marble + circle.popleft()

print(max(scores))