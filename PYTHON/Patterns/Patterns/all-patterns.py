number = int(input("Enter a number:"))

# Standing line
# for i in range(number):
#     print("*")

# # Slanting line
# for j in range(number):
#     print("*",end=" ")

# Box
for k in range(number):
    for l in range(number):
        if ((k == 0) or (l == 0) or (k == number-1) or (l == number-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()