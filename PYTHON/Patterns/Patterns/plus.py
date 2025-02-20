# Plus pattern

"""
  *
  *
*****
  *
  *
"""


size = int(input("Enter the size you want:"))

for i in range(size):
    for j in range(size):
        if i == size // 2:
            print('*', end='')
        else:
            if j == size // 2:
                print('*', end='')
            else:
                print(' ', end='')
    print()