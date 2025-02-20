# Using for loop

'''

1
12  
123 
1234
123456

'''

num = int(input("Enter the number : "))

for i in range(num):
    for j in range(1,i+1):
        print(j,end="")
    print()



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()