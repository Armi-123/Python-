user=int(input("Enter the value: "))
alpha=65

# 1,2 line
for i in range(user):
    for j in range(user-i):
        print(" ",end="")
    for n in range(i+1):
        print(chr(alpha+n),end=" ")
    print()   

# 1,2 line
for i in range(user):
    for j in range(i+2):
        print(" ", end="")
    for n in range((user-i)-1):
        print(chr(alpha+n), end=" ")
    print()