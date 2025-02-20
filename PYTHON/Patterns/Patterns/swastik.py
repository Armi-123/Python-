# Swastik Pattern

num=int(input("Enter any number:"))

for i in range (num):
    for j in range(num):
        # if (i == 2 or i == 4 or j == 0 or j == 2 or j == 4 or j == 3):
        if (i == 0):
            if (j == 0) or (j == 2) or  (j == 3) or (j == 4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if (i == 1):
            if (j == 0) or (j == 2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if (i == 2):
            if (j == 0) or (j == 1) or (j == 2) or (j == 3) or (j == 4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if (i == 3):
            if (j == 2) or (j == 4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        if (i == 4):
            if (j == 0) or (j == 1) or (j == 2) or (j == 4):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

