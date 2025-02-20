# bnak management system
import json

class Customer:
    def __init__(self, name, email, mobile, unique_id):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.unique_id = unique_id
        self.balance = 0
        self.save_data()
        self.load_data()
        
    def load_data(self):
        try:
            with open("bank_data.txt", "r") as file:
                customers = json.load(file)
        except FileNotFoundError:
            pass
        self.save_data()

    def save_data(self):
        with open("bank_data.txt", "w") as file:
            json.dump(customers, file)


    def deposit(self, d_amount):
        self.balance += d_amount
        self.d_amount = 0
        self.save_data()

    def withdraw(self, w_amount):
        if self.balance >= w_amount:
            self.balance -= w_amount
        else:
            print("Error")
        self.w_amount = 0
        self.save_data()

    def bank_statement(self):
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Mobile: {mobile}")
        print(f"Deposit amount: {self.d_amount}")
        print(f"Withdrawal amount: {self.w_amount}")
        print(f"Total amount: {self.balance}")

customers = {}

while True:
    print("\n1) Add customer")
    print("2) Deposit amount")
    print("3) Withdrawal amount")
    print("4) Initial balance")
    print("5) Bank statement")
    print("6) Exit")

    choice = int(input("\nChoose any one option: "))

    if choice == 1:
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        unique_id = input("Enter Unique ID: ")
        customers[unique_id] = Customer(name, email, mobile, unique_id)

    elif choice == 2:
        unique_id = input("Enter Unique ID: ")
        amount = float(input("Enter Deposit amount: "))
        customers[unique_id].deposit(amount)

    elif choice == 3:
        unique_id = input("Enter Unique ID: ")
        amount = float(input("Enter Withdrawal amount: "))
        customers[unique_id].withdraw(amount)

    elif choice == 4:
        unique_id = input("Enter Unique ID: ")
        print(f"Available balance: {customers[unique_id].balance}")

    elif choice == 5:
        unique_id = input("Enter Unique ID: ")
        customers[unique_id].bank_statement()

    elif choice == 6:
        print("exit....")
        break