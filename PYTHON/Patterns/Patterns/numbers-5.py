"""    
    1
   1 2
  1   2
 1     2
123456789

"""

# hollow number pyramid pattern
size = 5
for i in range(size):
    # print spaces
    for j in range(size - i - 1):
        print(" ", end="")

    # print numbers
    count = 1
    for k in range(2 * i + 1):
        if i == 0 or i == size - 1:
            print(count, end="")
            count += 1
        else:
            if k == 0 or k == 2 * i:
                print(count, end="")
                count += 1
            else:
                print(" ", end="")
    print()