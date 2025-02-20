user=int(input("Enter the value: "))

for i in range(user):
    for j in range(user):
        if i==0 or j==0 or i==user-1 or j==user-1:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()