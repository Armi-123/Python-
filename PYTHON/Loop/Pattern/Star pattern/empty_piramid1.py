user=int(input("Enter the value: "))

for i in range(user):
    for j in range(user-i):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==user-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()