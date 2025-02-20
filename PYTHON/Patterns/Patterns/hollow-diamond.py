# Hollow diamond star pattern

"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
"""



# num = int(input("Enter any number:"))

# # upward hollow pyramid
# for i in range(num):
#     for j in range(num - i - 1):
#         print(' ', end='')
#     for k in range(2 * i + 1):
#         if k == 0 or k == 2 * i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# # downward pyramid
# for i in range(num - 1):
#     for j in range(i + 1):
#         print(' ', end='')
#     for k in range(2*(num - i - 1) - 1):
#         if k == 0 or k == 2*(num - i - 1) - 2:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()








# Way 2
n = int(input("enter n:"))
s = 1
for row in range(1,n+1):
    # for space in range(n - row):
    #     print(" ",end='')
    if row == 1:
        print(" "*(n-row),end='')
        print('*')
    else:
        print(' '*(n-row),end='')
        print('*',end='')
        print(' '*s,end='')
        print('*')
        s+=2
s-=4
for row in range(n-1,0,-1):
    for space in range(n-row):
        print(' ',end='')
    if row==1:
        print('*')
    else:

        print('*',end='')
        print(' '*s,end='')
        print('*')
        s-=2