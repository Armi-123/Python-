# print("Welcome to Our Restaurant!")

# print("1. Pizza - $10")
# print("2. Burger - $8")
# print("3. Salad - $6")
# print("4. Pasta - $12")

# choice = input("Enter your choice (1-4): ")

# if choice == '1':
#     quantity = int(input("Enter the quantity: "))
#     total = quantity * 10
#     print("Your total is $", total)
# elif choice == '2':
#     quantity = int(input("Enter the quantity: "))
#     total = quantity * 8
#     print("Your total is $", total)
# elif choice == '3':
#     quantity = int(input("Enter the quantity: "))
#     total = quantity * 6
#     print("Your total is $", total)
# elif choice == '4':
#     quantity = int(input("Enter the quantity: "))
#     total = quantity * 12
#     print("Your total is $", total)
# else:
#     print("Invalid choice.")
# ////////
# print("Welcome to Our Restaurant!")

# # User 1
# print("\nUser 1:")
# print("1. Pizza - $10")
# print("2. Burger - $8")
# print("3. Salad - $6")
# print("4. Pasta - $12")

# choice1 = input("User 1, enter your choice (1-4): ")

# if choice1 == '1':
#     quantity1 = int(input("Enter the quantity: "))
#     total1 = quantity1 * 10
# elif choice1 == '2':
#     quantity1 = int(input("Enter the quantity: "))
#     total1 = quantity1 * 8
# elif choice1 == '3':
#     quantity1 = int(input("Enter the quantity: "))
#     total1 = quantity1 * 6
# elif choice1 == '4':
#     quantity1 = int(input("Enter the quantity: "))
#     total1 = quantity1 * 12
# else:
#     print("Invalid choice for User 1.")
#     total1 = 0

# # User 2
# print("\nUser 2:")
# print("1. Pizza - $10")
# print("2. Burger - $8")
# print("3. Salad - $6")
# print("4. Pasta - $12")

# choice2 = input("User 2, enter your choice (1-4): ")

# if choice2 == '1':
#     quantity2 = int(input("Enter the quantity: "))
#     total2 = quantity2 * 10
# elif choice2 == '2':
#     quantity2 = int(input("Enter the quantity: "))
#     total2 = quantity2 * 8
# elif choice2 == '3':
#     quantity2 = int(input("Enter the quantity: "))
#     total2 = quantity2 * 6
# elif choice2 == '4':
#     quantity2 = int(input("Enter the quantity: "))
#     total2 = quantity2 * 12
# else:
#     print("Invalid choice for User 2.")
#     total2 = 0

# # Calculate and display totals
# total = total1 + total2
# print("\nTotal for User 1: $", total1)
# print("Total for User 2: $", total2)
# print("Combined Total: $", total)
# ////////////
print("Welcome to Our Restaurant!")

# User 1
print("\nUser 1:")
print("1. Pizza - $10")
print("2. Burger - $8")

choice1 = input("User 1, enter your choice (1-2): ")

if choice1 == '1':
    print("Great choice! Pizza selected.")
    print("1. Large Pizza - $15")
    print("2. Medium Pizza - $12")
    size_choice = input("User 1, select pizza size (1-2): ")
    if size_choice == '1':
        price1 = 15
    elif size_choice == '2':
        price1 = 12
    else:
        print("Invalid choice for size.")
        price1 = 0
elif choice1 == '2':
    print("Nice! Burger selected.")
    print("Burgers come in one size.")
    price1 = 8
else:
    print("Invalid choice for User 1.")
    price1 = 0

# User 2
print("\nUser 2:")
print("1. Soda - $2")
print("2. Fries - $3")

choice2 = input("User 2, enter your choice (1-2): ")

if choice2 == '1':
    print("Refreshing choice! Soda selected.")
    price2 = 2
elif choice2 == '2':
    print("Yummy! Fries selected.")
    price2 = 3
else:
    print("Invalid choice for User 2.")
    price2 = 0

# Calculate and display totals
total = price1 + price2
print("\nTotal for User 1: $", price1)
print("Total for User 2: $", price2)
print("Combined Total: $", total)