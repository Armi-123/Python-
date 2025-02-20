user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(user):
        if i==user//2 or j==user//2 or (i==0 and j>=user//2) or (j==0 and i<=user//2) or (j==user-1 and i>=user//2) or (i==user-1 and j<=user//2):
            print("*",end=" ")
        else :
            print(" ",end=" ")

    print()