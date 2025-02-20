#  Accept the age of 4 people and display the younger one.


age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))
age4 = int(input("Enter age of person 4: "))

if age1 <= age2 and age1 <= age3 and age1 <= age4:
    print("persone one younger")    

elif age2 <= age1 and age2 <= age3 and age2 <= age4:
    print("persone two younger")   

elif age3 <= age1 and age3 <= age2 and age3 <= age4:
    print("persone three younger") 

else:
    print("persone four younger")