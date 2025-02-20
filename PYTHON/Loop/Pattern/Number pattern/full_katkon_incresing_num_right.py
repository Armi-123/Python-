user=int(input("Enter the value: "))

for i in range(user):
    for j in range(i,user):
        print(" ",end=' ')
    for n in range(i+1):
        print(" ",end=str(n+1))    
    print()