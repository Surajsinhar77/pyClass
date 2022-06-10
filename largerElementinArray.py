
# len(a)
#  23   2   34   234   23   25
#  0    1   2    3      4   5

# if 0 > 1:
#  max = ary[0]
# else:
#     max = ary[1]
#  max > 2
#   else:
#   max = ary[2]

# max > 3    234
# else:
#  max = ary[3]

# max >  4
# else:
#   max = ary[4]

# max >  5   234   ;   234 > 25
# else:
#   max = ary[5]

# print( max)

ary = [23,2,34,234,23,25] 

# max = ary[0]

# for i  in range(1,len(ary),1):
#     if  max>ary[i]:
#         continue
#     else:
#         max = ary[i]

# max = 23
#  i koh 1 to 6    incn 1
#  i = 2
#   23 > ary[1]  => 23 > 2
#   continue
#   i = 2
#   23 > ary[2]  => 23 > 34 
#   else:
#       max = ary[2]    = 34
#    
#   i = 3
#      34 > ary[3] => 34 > 234
#    else:
#    max  = ary[3]  = 234
#   i = 4
#   
#   234 > ary[4]  => 234 > 23 
#   continue
#   i = 5
#  234 > ary[5] => 234 > 25
#  continue
#  i = 6 

# print(max)
