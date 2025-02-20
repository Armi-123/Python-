user= int(input("enter the value: "))

for i in range(user-1):
    for j in range(i+1,user):
        print(" ",end=" ")
    for s in range(i):
        # print(" ",end="")
        print(" ",end=str(s+1))
    print()

for i in range(user):
    for j in range(i):
        print(" ", end=" ")
    for n in range((user-i)-1):
        print(" ", end=str(n+1))
    print()