num = 5

for i in range (1,num+1):
    for j in range (1,num+1):
        if (i == 1) or (j==3):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()