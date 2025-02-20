user=int(input("enter the value: "))

for i in range(user):
    for j in range(i,user):
        print(" ",end=" ")
    for s in range(2*i+1):
        print("",end="")
        print(" ",end=str(s+1))
    print()

for i in range(user-1,0,-1):
    for j in range(i,user+1):
        print(" ",end=" ")
    for n in range((2*i)-1,0,-1):
        print(" ",end=str(n))
    print()