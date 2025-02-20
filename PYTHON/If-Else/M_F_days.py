# "Accept the age, gender (M,F), number of days and display the wages accordingly:                                         
#  Age                            Gender                        Wage/Day
# >=18 and <30                M                                  700
#     __                               F                                  750
# >=30 and <=40               M                                  800
#     __                               F                                  850
# "

age = int(input("Enter age: "))
gender = (input("Enter M/F: "))
day=int(input("Enter working days: "))

if age >= 18 and age < 30:
    if gender == "male":
        income = 700
    elif gender == "female":
        income = 750
        
elif age >= 30 and age <= 40:
    if gender == "male":
        income = 800
    elif gender == "female":
        income = 850

total = day * income 
print("your income: ",total)