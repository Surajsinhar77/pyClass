ary = [-34,24,-1,42,4,-6,2]

countNeg = 0
i = 0
while i < len(ary):
    if ary[i] < 0:
        countNeg = countNeg + 1
    i= i+1

# print(countNeg)

j =0
while j < countNeg:
    if ary[j] < 0:
        j= j+1
        continue
    else:
        k = j+1             # search after ary[j]  
        while k < len(ary): #
            if ary[k] < 0:
                temp = ary[j]
                ary[j] = ary[k]
                ary[k] = temp
            k= k+1
    j = j+1

# print(countNeg)
print(ary)
