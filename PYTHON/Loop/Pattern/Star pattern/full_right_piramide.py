user=int(input("Enter the value: "))

# 1,3 star
for i in range(user):
    for j in range(i+1):
        print('*', end=" ")
    print()

for i in range(user):
    for j in range(user-i-1):
        print('*', end=" ")
    print()

# 1,2 star 
