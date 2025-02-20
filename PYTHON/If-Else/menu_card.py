##  Simple Menu Selection  ##

# print("a = panjabi food")
# print("b = gujarati food")
# print("c = south food")

# # select food
# user = input("enter any one a,b,c food = ")

# panjabifood = "a" 
# gujaratifood ="b"
# southfood ="c"

# if user == panjabifood: 
#     print("h = paneerhandi" ,"k = kajukari")

# elif user == gujaratifood :    
#     print("s = sev tomato","p = potato")

# elif user == southfood :    
#     print("g = green gotala","r = raja rani")
# else:
#     print("please select courrect item")

# # select items
# abc = input("please select any one item = ")    

# paneerhandi = "h"
# kajukari = "k"

# greengotala = "g"
# rajarani = "r" 

# sevtomato = "s"
# potato = "p"

# if abc == paneerhandi :
#     print("price : ",219)
# elif abc == kajukari :
#     print("price : ",249)   

# elif abc == sevtomato :
#     print("price : ",149)
# elif abc == potato :
#     print("price : ",99)     
   
# elif abc == greengotala :
#     print("price : ",229)
# elif abc == rajarani :
#     print("price : ",279)    
# else :
#     print("please select courrect item")


# /// 2nd typ of menu_card

# User 1
print("User 1:")
print("a = panjabi food")
print("b = gujarati food")
print("c = south food")

user = input("user choice a food : ")

if user == 'a':
    print("1. kajukari - 249")
    print("2. paneer handi - 199")
    choice = input("choice item (1-2): ")
    if choice == '1':
        price1 = 249
    elif choice == '2':
        price1 = 199
    else:
        print("Invalid choice.")
        price1 = 0
elif user == 'b':
    print("1.sev tomato - 149")
    print("2. potato - 99")
    choice = input("choice item (1-2): ")
    if choice == '1':
        price1 = 149
    elif choice == '2':
        price1 = 99
    else:
        print("Invalid choice.")
        price1 = 0
elif user == 'c':
    print("1. green gotala - 249")
    print("2. raja_rani - 229")
    choice = input("choice item (1-2): ")
    if choice == '1':
        price1 = 249
    elif choice == '2':
        price1 = 229
else:
    print("Invalid choice.")
    price1 = 0

# User 2
print("\nUser 2:")
print("1. cold-drinks - 20")
print("2. buttermilk - 25")

choice2 = input("User choice drink: ")

if choice2 == '1':
    print("'cold-drinks selected.'")
    price2 = 20
    quantity = int(input("Enter the quantity: "))
    total1 = quantity * 20
elif choice2 == '2':
    print("'buttermilk selected.'")
    price2 = 25
    quantity = int(input("Enter the quantity: "))
    total1 = quantity * 25
else:
    print("Invalid choice.")
    total1 = 0

# Calculate and display totals
total = price1 + total1
print("\nTotal for User 1: ", price1)
print("Total for User 2: ", total1)
print("Total Bill: ", total)