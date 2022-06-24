
# def fun1():
#     pass
# fun1()


# def cal(x):

#     def add(a, b):
#         return a+b

#     def sub(a, b):
#         return a-b

#     def mult(a, b):
#         return a*b
    
#     def div(a, b):
#         return a/b

#     a = int(input("Enter num1 : "))
#     b = int(input("Enter num2 : "))
    
#     if(x == 'add'):
#         print(add(a,b))
#     elif(x=='sub'):
#         print(sub(a,b))
#     elif(x == 'mult'):
#         print(mult(a,b))
#     else:
#         print(div(a,b))
    
# print("\n")
# print("Give add for addition \nGive sub for subtraction \nGive mult for multipliacation \nGive div for division")

# x = input("Enter the value : ")

# cal(x)

# def cal(x):

#     def add(a, b):
#         print(a+b)

#     def sub(a, b):
#         print(a-b)

#     def mult(a, b):
#         print(a*b)
    
#     def div(a, b):
#         print(a/b)

#     a = int(input("Enter num1 : "))
#     b = int(input("Enter num2 : "))
    
#     if(x == 'add'):
#         add(a,b)
#     elif(x=='sub'):
#         sub(a,b)
#     elif(x == 'mult'):
#         mult(a,b)
#     elif(x=='div'):
#         div(a,b)
    
# print("\n")
# print("Give add for addition \nGive sub for subtraction \nGive mult for multipliacation \nGive div for division")

# x = input("Enter the value : ")

# cal(x)

# 1 2 3 4 5 6 7 8 9 10

# sum = 0
# for i in range(1,11,1):
#     sum = sum + i

# print(sum)


def addcountnum(x):
    if(x==0):
        return x
    sum = addcountnum(x-1)
    sum = int(sum)+x 
    return sum

ans = addcountnum(10)
print(ans)



