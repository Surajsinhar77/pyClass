
ary = [35,31,34,53,45,45,135]

max = ary[0]
maxLoc = ' '
i = 1
secMax = 0
# j= len(ary)-1
while i<len(ary): # for i in range(1, len(ary, 1)):
    if(max > ary[i]):
        i+=1
        continue
    else:
        maxLoc = i
        max = ary[i]
    i+=1 # i = i+1

j=0
while j<len(ary):
    if( secMax > ary[j] or ary[j] == max):
        j+=1
        continue
    else:
        secMax = ary[j]
    j+=1

print(secMax)

print(type(maxLoc))
print(max,maxLoc)