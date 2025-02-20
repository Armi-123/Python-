# Mirror image of swastik

# n = 5  

# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2 or (i == 0 and j < n // 2) or (i == n - 1 and j > n // 2) or (j == 0 and i > n // 2) or (j == n - 1 and i < n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


num=int(input("Enter a number :")) 

if num % 2 == 0:
    div = (num/2) 
else:
    div = (num // 2) + 1 

for i in range(num):
    for j in range(num):
        if i == div - 1 or j == div - 1 or (i == 0 and j < div - 1) or (i == num-1 and j > div - 1) or (j==0 and i>div-1) or (j==num-1 and i<div - 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()