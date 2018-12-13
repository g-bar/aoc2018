import numpy as np
from collections import *
from itertools import *
import re
import datetime

with open('day4_input.txt') as f:    
    theinput = f.read().splitlines()

##Part 1

datepattern = re.compile(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\]")
records = []
for record in theinput:
    date = map(int,datepattern.search(record).groups())
    d = datetime.datetime(*date)
    records.append((d,record[19:]))
records = sorted(records)

count = Counter()
perminute = defaultdict(lambda: defaultdict(int))
for d, record in records:
    shift = re.findall(r'\d+', record)
    if shift:
        sleep = False
        guard = int(shift[0])
    sleep = 'sleep' in record
    awake = 'wakes' in record
    if sleep:
        sleepstart = d
    
    if awake:                
        for minute in range(sleepstart.minute, d.minute):            
            count[guard]+=1
            perminute[guard][minute]+=1

guard_most_sleep = max(count.items(),key=lambda c: c[1])[0]
most_slept_minute = max(perminute[guard_most_sleep].items(), key=lambda c: c[1])[0]

print(guard_most_sleep * most_slept_minute)

## This solution doesn't need to keep two counts 
most_sleep = max(perminute.items(), key=lambda item: sum(item[1].values()))
print(most_sleep[0] * max(most_sleep[1].items(), key= lambda item:item[1])[0])

#Part 2
times = 0
for guard in perminute:
    minutes = perminute[guard]
    most_slept_minute = max(minutes.items(), key = lambda t: t[1])

    times_for_guard = most_slept_minute[1]
    whichminute = most_slept_minute[0]
    
    if times_for_guard >= times:
        times = times_for_guard
        theminute = whichminute
        theguard = guard

print(theminute*theguard)
    