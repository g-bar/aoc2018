inputstr = open('day5_input.txt').read()
theinput = list(inputstr)
deletions = True
uniques = set(inputstr.lower())
def collapse(polymer):
    deletions = True
    while deletions:
        i=0
        deletions = 0
        while i<(len(polymer)-1):
            first, second = polymer[i:i+2]
            if (first != second) and (first.lower() == second.lower()):
                del polymer[i:i+2]
                deletions+=1
            else: 
                i+=1
    return len(polymer)
    
polymers = [[l for l in theinput if not l.lower() == filtered] for filtered in uniques]

#Part1
print(collapse(theinput))

#Part2
print(min(collapse(polymer) for polymer in polymers))
    