# Diamond star pattern

"""

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

"""

# n = 5

# # upward pyramid
# for i in range(n):
#     for j in range(n - i - 1):
#         print(' ', end='')
#     for j in range(2 * i + 1):
#         print('*', end='')
#     print()

# # downward pyramid
# for i in range(n - 1):
#     for j in range(i + 1):
#         print(' ', end='')
#     for j in range(2*(n - i - 1) - 1):
#         print('*', end='')
#     print()



                                        # OR




num = 5
for i in range (num-1):
    for j in range (num-i):
        print(" ",end=" ")
    for k in range (j,num+i):
        print("*",end=" ")
    print()
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(j,num):
        print("*",end=" ")
    for l in range(num-i-1):
        print("*",end=" ")
    print()




                                        # OR



# num = 5
# for i in range (num-1):
#     for j in range (num-i):
#         print(" ",end=" ")
#     for k in range (num-j-1):
#         print("*",end=" ")
#     for l in range (i+1):
#         print("*",end=" ")
#     print()
# for i in range(num):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(num-i-1):
#         print("*",end=" ")
#     for l in range(num-i):
#         print("*",end=" ")
#     print()
