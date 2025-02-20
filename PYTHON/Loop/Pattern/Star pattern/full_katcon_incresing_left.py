user=int(input("Enter the value: "))

# continue
for i in range(user):
    for j in range(i+1):
        print("*",end="")
    print()

# space katkon
for i in range(user):
    for j in range(i+1):
        print("*",end=" ")
    print()