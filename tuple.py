# Tuple  is unmutable data type

tup = ("32422","name",'name',89989,45,5,"32422","32422",32422)

hg = []

hg = list(tup)

# print(type(hg))
hg[0] = "89329823"
# print(hg)

tup = tuple(hg)

print(tup)

# print(type(tup))

for i in range(0, len(tup),1):
    print(tup[i])






# print(tup.count(5))
# print(tup)

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])


# print(type(tup))