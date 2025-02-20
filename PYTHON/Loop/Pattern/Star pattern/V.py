user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(2*user-i):
        if i==j or i+j==2*user-2:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()