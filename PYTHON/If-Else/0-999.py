#Write a program that inputs an integer in range 0-999 and then prints if the integer entered is 1/2/3 digit number.

a = int(input("Enter a value of(0,999) : "))

if a <= 999 :
    print("your number is = ",(a%1000)//100,"/",(a%100)//10,"/",a%10)
else : 
    print("enter the currect number ")

#
num = int(input("Enter an integer between 0 and 999: "))

if 0 <= num <= 9:
    print("The entered number is a 1-digit number.")
elif 10 <= num <= 99:
    print("The entered number is a 2-digit number.")
elif 100 <= num <= 999:
    print("The entered number is a 3-digit number.")
else:
    print("Invalid input. Please enter an integer between 0 and 999.")
