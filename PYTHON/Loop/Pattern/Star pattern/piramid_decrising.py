user=int(input("Enter the value: "))

# 1,2 star
for i in range(user):
    for j in range(i):
        print("",end=" ")
    for n in range(i,user):
        print("*",end="")
        print("",end=" ")
    print()

# 1,3 star
for i in range(1,user+1):
    for j in range(i-1):
        print(" ",end="")
    for n in range(2*(user-i)+1):
        print("*",end="")
        print("",end="")
    print()