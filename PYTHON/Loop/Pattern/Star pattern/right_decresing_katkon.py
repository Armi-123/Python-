user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(i+1):
        print(" ",end=" ")
    for n in range(i,user):
        print("*",end=" ")
    print()