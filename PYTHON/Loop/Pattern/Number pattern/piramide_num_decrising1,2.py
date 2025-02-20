user=int(input("Enter the value: "))
 
# last line constant
for i in range(user+1):
    for j in range(i+1):
        print(" ",end="")
    for n in range(i,user):
        print(" ",end=str(n+1))
    print()

# first line constant
for i in range(user+1):
    for j in range(i):
        print("", end=" ")
    for n in range((user-i)):
        print(" ", end=str(n+1))
    print()