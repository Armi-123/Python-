user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(user):
        if j==0 or (i==user-1 and j<=user//2):
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()