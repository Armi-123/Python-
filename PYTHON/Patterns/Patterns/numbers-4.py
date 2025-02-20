"""
123456789
 1234567
  12345
   123
    1
"""

# n = 5 

# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2 * (n-i) - 1):
#         print(k+1,end=" ")
#     print()

n = 5 
for i in range(n):
    for j in range(i+1):
        print("-",end="")
    for k in range(1,n-i+1):
        print(k,end="")
    for l in range(1,n-i):
        print(k+l,end="")
    print()