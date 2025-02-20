# Write a program in which you have to take 2 variables and user input for them and check the largest one 
# ,the smallest one and check if the first variable is divisible by the second one.

a = int(input("enter first value = "))
b = int(input("enter second value = "))

if a > b : 
    print("A is Largest" )
    if a % b == 0 :
        print("A is Divisible by B")
    else :
        print("A is NOT Divisible by B")    
else :
    print("B is largest")