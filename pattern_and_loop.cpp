# cook your dish here

# *
# **
# ***
# ****
# *****


# *****
# ****
# ***
# **
# *


# for i in range (start, end , direction)
#                 0        6   1
#                 10       0   -1

#       *  
#      **
#     ***
#    ****
#   *****



#  i      0  to 5
#  j      5  to  1



# for i in range(0,5,1):             # 0  1 2 4 
#      for j in range (5-i,0,-1):    # 5-0   5-4 = 1-10
#           print("*", end=" ")      # *****
#      print("\n")                   #****
#                                    #***
                                   
                                   #*
                                   
                                   
                                   
# for i in range (0, 5, 1):
#      for j in range(4-i, 0, -1):
#           print(" ", end="")
     
     
#      for k in range(0, i+1, 1):
#           print("*", end="")
          
#      print("\n")                                               

#  kkkkkkk*
#  kkkkkk***
#  kkkk******
#  kkk********
#  kk**********
#  k************
#  **************
#  k*************
#  kk***********
#  kkk*********  
#  kkkk*******  
#  kkkkk*****  
#  kkkkkk***  
#  kkkkkkk* 
#    
#    
#    
#      

#  up triange code

# i=0
# while(i<6):
#    k=(7-1)-i
#    while(k>0):
#         print(' ',end=' ')
#         k=k-1
#    j=i+1
#    while(j>0):
#         print('*',end=' ')
#         j=j-1
#    # i=i+1
#    j=0
#    while j<i:
#         print('*',end=' ') 
#         j=j+1
#    print('\n')
#    i=i+1   


# for h in range(0,8+7,1):
#      print("*", end=" ")
# print("\n")
# down triangle code 

# for g in range (0,7,1):
#      for j in range(0,g,1):
#           print("k", end =" ")
     
#      for k in range(7-g,0,-1):
#           print("*" , end=" ")
     
#      for l in range(7-g,1,-1):
#           print('*' , end= ' ')
          
#      print("\n")
     
     

# ******* *******
# *** *** *** ***
# **   ** **   **
# *     * *     *

for i in range (0 ,5, 1):
     for j in range (5-i,0,-1):
          print("*" , end=' ')
     
     for k in range (0,i,1):
          print(" ", end=" ")
          
     for l in range (1,i,1):
          print(" ", end=" ")
     
     h=5
     
     if i == 0:
          h = h-i-1
     else:
          h = h-i
     
     for j in range (h,0,-1):
          
          print("*" , end=' ')
          
     
    
          
     print("\n")
     






