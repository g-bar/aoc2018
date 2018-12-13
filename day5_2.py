inputstr = "dabAcCaCBAcCcaDA"
theinput = list(inputstr)
deletions = True
while deletions:
    i=0
    deletions = 0
    while i<(len(theinput)-1):
        first, second = theinput[i:i+2]
        if (first != second) and (first.lower() == second.lower()):
            del theinput[i:i+2]
            deletions+=1
            i-=1
        i+=1
    

print(''.join(theinput))



    