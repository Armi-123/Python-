user=int(input("Enter the value: "))

if user % 2==0:
    user+=1
 
for i in range(user):
    for j in range(user):
        if i==user//2 or j==user//2 :
            print("*",end="")
        # if i==user//2 or j==user//2 :
        #     print("*",end="")        
        else :
            print(" ",end=" ")

    print()