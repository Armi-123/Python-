# piramid

user=int(input("Enter the value: "))

# 1 ,2 star 
for i in range(user):
    for j in range(i,user+1):
        print("",end=" ")
    for n in range(i+1):
        print("*",end="")
        print("",end=" ")
    print()

# 1,3 star
for i in range(1,user+1):
    for j in range(user - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()