# Using For loop

"""
*******
*  *  *
*******
*  *  *
*******

"""




# Define the number of rows and columns
rows = int(input("Enter rows:"))
columns = int(input("Enter columns:"))

# Loop to print the pattern
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('* ' * columns)
    else:
        print('*  *  *')





num = int(input("Enter any number:"))

if num % 2 == 0:
    num = num - 1


for i in range (num):
    for j in range(num):
        if (i == 0 or i == num//2 or i == num - 1 or j == 0 or j == num//2 or j == num - 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
