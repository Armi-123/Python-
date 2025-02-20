user=int(input("Enter the value: "))

# first line
for i in range(user):
    for j in range(i):
        print(" ", end=" ")
    for n in range(2*(user-i)-1):
        print(" ", end=str(n+1))
    print()

# last line constant
for i in range(user):
    for j in range(i+1):
        print(" ",end=" ")
    for n in range(2*(user-i)-1):
        print(" ",end=str(n+1))
    print()