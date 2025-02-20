# Age Category Classifier:

age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
  print("Your age group is Child")

elif age >= 13 and age <= 19:
  print("Your age group is Teenager")

elif age >= 20 and age <= 59:
  print("Your age group is Adult")
  
else:
  print("Your age group is Senior Citizen")