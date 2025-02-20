user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(user):
        if j==0 or j==user-1 or (i==j and i>=user//2) or (i+j==user-1 and j<=user//2):
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()