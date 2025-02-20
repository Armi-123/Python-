# Write a program to accept runs from the user and display the result as per the following criteria:                Marks                                                  Grade
# >=100                                                  Century
# >=50                                                     Fifty
# below 50                                Neither a century nor fifty

user = int(input("Enter your runs: "))

if user>= 100 :
    print("century")

elif user>= 50 :
    print("fifty")   

elif  user <= 50:
    print("Neither a century nor fifty")