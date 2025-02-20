a = int(input("enter the value: "))

for i in range(a):
    for j in range(i,a):
        print(" ",end="")
    for s in range(i+1):
        print("",end="")
        print(" ",end=str(s+1))
    print()