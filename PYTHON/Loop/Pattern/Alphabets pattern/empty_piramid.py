user=int(input("Enter the value: "))
alpha = 65
num = 0

for i in range(user):
    for j in range(user-i-1):
        print(" ", end="")
    for k in range(2*i+1):
        if i==0 or i==user-1:
            print(chr(alpha + num), end="")
            num += 1
        else:
            if k==0 or k==2*i:
                print(chr(alpha + num), end="")
                num += 1
            else:
                print(" ", end="")
    print()