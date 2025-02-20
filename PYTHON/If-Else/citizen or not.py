#  Write a program to check whether the person is senior citizen or not.


age = int(input("Enter you age: "))

if age >= 60:
    print("You are a senior citizen")
else:
   print("You are not a senior citizen")

# use year...
birth_year=int(input( "Enter year of birth: " ))
current_year=int(input( "Enter current year: " ))

age=current_year-birth_year
print("Age:",age)

if(age>= 60 ):
    print( "Senior Citizen" )

else:
    print( "Not a senior citizen" )