# "Write a program to accept percentage and display the category as per the following criteria:

a = int(input("enter the percentage = "))

if a < 40 :
    print("your category is 'Failed'")

if 40 <= a < 55 :
    print("your category is 'Fair'") 

if 55 <= a < 65 :
    print("your category is 'Good'") 

if a >= 65 :
    print("youe category is 'Excellent'")