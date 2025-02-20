 # Display the last digit of the given number and check whether it is divisible by 3 or not.

a = int(input("enter the number is :"))
b = a % 3
print(b)
if b%3 == 0:
    print(b , "is Divisible by 3")
else :
    print(b ,"is Not Dvisible by 3")