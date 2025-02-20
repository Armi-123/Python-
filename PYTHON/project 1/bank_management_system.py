# Bank management system

import json

try:
    with open("customers.json","r") as file:
        customers = json.load(file)
except FileNotFoundError:
    customers = {}

while True:
    print("\n1) Add customer")
    print("2) Deposit amount")
    print("3) Withdrawal amount")
    print("4) Initial balance")
    print("5) Bank statement")
    print("6) Exit")

    user = input("\nChoose any one option: ")

    if user == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        mobile = input("Enter mobile: ")
        unique_id = input("Enter unique ID: ")
        customers[unique_id] = {"name": name, "email": email, "mobile": mobile, "balance": 0}
        print("Customer added successfully!")
        with open("customers.json", "w") as file:
            json.dump(customers,file)

    elif user == "2":
        unique_id = input("Enter unique ID: ")
        if unique_id in customers:
            d_amount = float(input("Enter deposit amount: "))
            customers[unique_id]["balance"] = d_amount
            print("Amount deposited successfully!")
            with open("customers.json", "w") as file:
               json.dump(customers,file)
        else:
            print("unique id not found!")

    elif user == "3":
        unique_id = input("Enter unique ID: ")
        if unique_id in customers:
            w_amount = float(input("Withdrawal amount: "))
            if customers[unique_id]["balance"] >= w_amount:
                customers[unique_id]["balance"] -= w_amount
                print("Amount withdrawn successfully!")
                with open("customers.json", "w") as file:
                    json.dump(customers,file)
            else:
                print("Insufficient balance!")
        else:
            print("unique id not found!")

    elif user == "4":
        unique_id = input("Enter unique ID: ")
        if unique_id in customers:
            print("Available balance:", customers[unique_id]["balance"])
        else:
            print("unique id not found!")

    elif user == "5":
        unique_id = input("Enter unique ID: ")
        if unique_id in customers:
            print("\nName:", customers[unique_id]["name"])
            print("Email:", customers[unique_id]["email"])
            print("Mobile:", customers[unique_id]["mobile"])
            print("Deposit amount:",d_amount)
            print("Withdrawal amount: ",w_amount)
            print("Total amount:", customers[unique_id]["balance"])
        else:
            print("unique id not found!")

    elif user == "6":
        print("Exit...")
        break

    else:
        print("Invalid choice.")