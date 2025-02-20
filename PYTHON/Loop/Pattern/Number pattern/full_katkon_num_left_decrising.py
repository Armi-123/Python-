user=int(input("Enter the value: "))

for i in range(user):
    for j in range(i,user):
        print(" ",end=str(j))
    print()