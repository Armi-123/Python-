user = int(input("Enter the value: "))

for i in range(user,0,-1):
    for j in range(user-i):
        print(" ", end="")
    for n in range(2*i-1):
        if n == 0 or n == 2*i-2 or i == user:
            print("*", end="")
        else:
            print(" ", end="")
    print()