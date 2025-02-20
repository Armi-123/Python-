# number pyramid pattern

"""
    1
   123
  12345
 1234567
123456789

"""

size = 5
for i in range(size):
    # print spaces
    for j in range(size - i - 1):
        print(" ", end="")
    # print numbers
    for k in range(2 * i + 1):
        print(k+1, end="")
    print()

                    # OR

# n = 5  # Change this value to control the number of rows

# for i in range(1, n + 1):
#     # Print spaces before the numbers
#     for j in range(n - i):
#         print(" ", end="")

#     # Print the numbers in ascending order
#     for j in range(1, i+1):
#         print(j, end="")

#     # Print the numbers in descending order (excluding 1 for the first row)
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     # Move to the next line after each row
#     print()
