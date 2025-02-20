"""
ABCDEFGHI
 ABCDEFG
  ABCDE
   ABC
    A
"""

# reverse alphabet pyramid pattern
size = int(input("Enter size: "))
alpha = 65

for i in range(size):
    # print spaces
    for j in range(i):
        print(" ", end="")
    # print alphabets
    for k in range(2 * (size - i) - 1):
        print(chr(alpha + k), end="")
    print()