user=int(input("Enter th value: "))

for i in range(user-1):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(user-i)-1):
        print("*", end="")
    print()

for i in range(user):
    for j in range(user-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
