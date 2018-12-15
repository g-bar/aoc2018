input = '99999'

length = len(str(input))
scores = [3,7]
digits = [int(n) for n in str(input)]
elf1 = 0
elf2 = 1

cond1 = digits != scores[-length:]
cond2 = digits != scores[-length-1:-1]

while cond1 and cond2  :
    total = scores[elf1] + scores[elf2]
    new = divmod(total, 10) if total >= 10 else (total,)
    
    scores.extend(new)    
    
    
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores)
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores)
    

    cond1 = digits != scores[-length:]
    cond2 = digits != scores[-length-1:-1]

if not cond1:
    print(len(scores[:-length]))
elif not cond2:
    print(len(scores[:-length-1]))