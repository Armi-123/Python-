user=int(input("Enter the value: "))
 
# same line
for i in range(user):
    for j in range(i+1):
        if j == 0 or j == i or i == user-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# bottam 2* line
for i in range(user):
    for j in range(i+1):
        if j==0 or j==i or i==user-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
