user=int(input("enter the value: "))

for i in range(user):
    for j in range(i,user):
        print(" ",end=" ")
    for s in range(2*i+1):
        print("",end="")
        print(" ",end=str(s+1))
    print()