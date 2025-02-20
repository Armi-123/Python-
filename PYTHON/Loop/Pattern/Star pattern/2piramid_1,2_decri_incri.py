user=int(input("Enter the value: "))

for i in range(user):
    for j in range(i+1):
        print("",end=" ")
    for n in range(i,user):
        print("*",end="")
        print("",end=" ")
    print()

for i in range(user-1):
    for j in range(i+1,user):
        print("",end=" ")
    for n in range(i+2):
        print("*",end="")
        print("",end=" ")
    print()