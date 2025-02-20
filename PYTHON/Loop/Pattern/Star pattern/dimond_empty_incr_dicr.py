user=int(input("Enter the value: "))

for i in range(user):
    for j in range(user-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(user-1,0,-1):
    for j in range(user-i):
        print(" ", end="")
    for n in range(2*i-1):
        if n == 0 or n == 2*i-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()