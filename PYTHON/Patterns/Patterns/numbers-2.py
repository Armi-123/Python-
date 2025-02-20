# Right number triangle pattern

"""
    1
   12
  123
 1234
12345
"""

size = 5
for i in range(size):
    # print spaces
    for j in range(1, size - i):
        print(" ", end="")
    # print numbers
    for k in range(i + 1):
        print(k + 1, end="")
    print()