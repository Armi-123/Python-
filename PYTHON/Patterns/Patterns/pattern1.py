# Using For loop

'''

$ $ $ $ $ $
$ $ $ $ $ $
$ $ $ $ $ $
$ $ $ $ $ $
$ $ $ $ $ $

'''

rows = int(input("Enter the rows you want in the pattern : "))
columns = int(input("Enter the columns you want in the pattern : "))


for row in range(rows):
    for column in range(columns):
            print("*",end= " ")
    print()