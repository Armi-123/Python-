num=int(input("Enter a number :"))

if num%2==0:
    div = (num/2) 
else:
    div = (num // 2) + 1 

for i in range(1,num+1):
    for j in range(1,num+1):
        if ((i==num and j<=div) or (j==num and i>=div) or i==div or (j==1 and i<=div) or (i==1 and j>=div) or j==div):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")


# n=5
# for i in range(n):
#     for j in range(n):
#         if i == n // 2 or j == n // 2 or (i == 0 and j >= n // 2) or (i == n - 1 and j <= n // 2) or (j == 0 and i <= n // 2) or (j == n - 1 and i >= n // 2):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

