# Write a program to calculate the electricity bill (accept number of unit from the user) as per the following criteria:    Unit                                                    Price
# First 100 units                                        no charge
# Next 100 unuits                                        Rs 5 per unit 
# After 200 units                                        Rs 10 per unit 
# (For example: IF input unit is 350 than total bill amount is Rs2000)

user = int(input("Enter electricity units : "))

if user <= 100 :
    charges = "no charge"
    
elif user <= 200 :
    charges = (user-100) * 5  

elif  user >= 200:
    charges = 100 * 5 + (user-200) * 10
    print(charges)