user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(user):
        if j==user//2-1 or (i==j and j>=user//2) or (i+j==user-1 and i<=user//2):
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()