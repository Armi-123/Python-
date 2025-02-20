user=int(input("Enter the value: "))
alpha = 65
num = 0

for i in range(user):
    for j in range(user-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print(chr(alpha+num), end="")
            num += 1
        else:
            print(" ", end="")
    num = 0
    print()

for i in range(user-1):
    for j in range(i+1):
        print(" ", end="")
    for j in range(2*(user-i-1)-1):
        if j == 0 or j == 2*(user-i-1)-2:
            print(chr(alpha+num), end='')
            num += 1
        else:
            print(' ', end='')
    num = 0
    print()