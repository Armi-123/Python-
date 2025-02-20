# Write a program to accept percentage from the user and display the grade as per the following criteria:
# Marks                                       Grade
# >90                                              A
# >80 and <90                                B
# >=60 and <80                              C
# below 60                                      D

user = int(input("Enter your marks: "))

if user>= 90 :
    print("grade A")

elif user>= 80 and user<= 90:
    print("grade B")   

elif user>= 60 and user<= 80:
    print("grade C") 

elif  user <= 60:
    print("grade D") 