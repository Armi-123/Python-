# decresing

user=int(input("Enter the value: "))
alpha = 65

# 1,3 line
for i in range(user):
    for j in range(i):
        print(" ", end="")
    for n in range(2*(user-i)-1):
        print(chr(alpha+n), end="")
    print()

# 1,2 line
for i in range(user):
    for j in range(i):
        print(" ", end="")
    for n in range((user-i)-1):
        print(chr(alpha+n), end=" ")
    print()