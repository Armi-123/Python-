user = int(input("enter the value: "))


for i in range(user):
    for j in range(i,user):
        print(" ",end=' ')
    for n in range(i+1):
        print("*",end=" ")
    for a in range(i+1):
        if i == a+n:
            print(" ",end=' ')
        print("*",end=" ")                          
    print()
print()

for i in range(user):
    for j in range(i+1):
        print(" ",end=' ')
    for n in range(i,user):
        print("*",end=" ")
    for a in range(i,user):
        if i == a:
            print(" ",end=' ')
        print("*",end=' ')                     
    print()