# "Accept the following from the user and calculate the percentage of class attended:1)Total number of working days 
# 2)Total number of days for absent. After calculating percentage show that,if the percentage is less than 75,than student will not be able to sit in exam.

# Take working days and absent days from the user , count present days with help of it and then count percentage of working days , if per > 75 you are eligible for exam otherwise not...

a = int(input("enter a total working days = "))
b = int(input("enter a absent days = "))

c = a - b 
print("total present days = ",c)
d = (c * 100 )/ a
print (d)

if 75 < d :
    print("you are eligible for exam")
else :
    print("you are NOT eligible for exam")