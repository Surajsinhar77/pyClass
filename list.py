

# print(a[::-1])

# for i in range(len(a)-1,0-1,-1):
    # print(a[i] , end=' ')

# print("\n")

# Liner Serch 

# var = int(input("Enter a vale to search : " ))  # 5
# for i in range(0,len(a),1):

#     if(var==a[i]): # 7==a[0]  7==1
#         print(" Yes , i found the  element at ",i)
#         break
#     else:
#         if(i==len(a)-1):
#             print("Your value is not present in List ")
        
# print(a)

# insert a value in list
# value = int(input("Enter a value to a insert : "))

# a.append(value)
# a.reverse()
# a.remove(56)
# a.remove(5)
# a.sort()
# a.reverse()

# print(a[2:7])
# print(a[::-1])
# print(a[0:4])
# print(a[-1:])
# print(a[2:])
# print(a[:-6:-1])


# Bubble sort
a  = [1,5,36,46,5,6,56,8,9]

for k in range(0,len(a),1):
    for i in range(0,len(a)-k-1,1):
        if(a[i] > a[i+1]):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
print(a)



# Time complixity o(n2)





# j =  10
# for i in range(0,11,1):
#     # print("\t\t")
#     print(i, end =" ")
#     print("\t\t")
#     print(j, end =" ")
#     j = j+1

    



