"""
*       *     
*       *     
*       *     
* * * * *     
*       *     
*       *     
*       * 

"""

# num =  7

# for j in range (1,num+1):
#     for i in range (1,num+1):
#         if (i == 1 or i == 5) or (j == 4 and i > 1 and i < 6):
#             print("*",end=" ")
#         else:
#             print(" ", end=" ")
#     print()




num = int(input("Enter any number:"))

if num % 2 == 0:
    num = num - 1
    
for i in range(num):
    for j in range(num):
        if j == 0 or j == num - 1 or i == num // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()