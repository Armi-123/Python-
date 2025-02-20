# incresing

user=int(input("Enter the value: "))
alpha=65

# 1,3 line
for i in range(user):
    for j in range(user-i):
        print(" ",end=" ")
    for n in range(2*i+1):
        print(chr(alpha+n),end=" ")
    print()

# 1,2 line
for i in range(user):
    for j in range(user-i):
        print(" ",end="")
    for n in range(i+1):
        print(chr(alpha+n),end=" ")
    print()   