import json
class Bank:
    def __init__(self):
        self.customers = {}
        self.balance = {}
        self.load_data()

    def load_data(self):
        try:
            with open("bank_data.txt", "r") as file:
                data = json.load(file)
                self.customers = data.get("customers", {})
                self.balance = data.get("balance", {})
        except FileNotFoundError:
            pass

    def save_data(self):
        with open("bank_data.txt", "w") as file:
            data = {"customers": self.customers, "balance": self.balance}
            json.dump(data, file)

    def add_customer(self):
        customer_name = input("Enter customer name: ")
        self.customers[customer_name] = []
        self.balance[customer_name] = 0
        print(f"Customer {customer_name} added successfully.")
        self.save_data()

    def deposit_amount(self):
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter amount to deposit: "))
        self.balance[customer_name] += amount
        self.customers[customer_name].append(f"Deposited: {amount}")
        print(f"Amount {amount} deposited successfully.")
        self.save_data()

    def withdrawal_amount(self):
        customer_name = input("Enter customer name: ")
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance[customer_name]:
            print("Insufficient balance.")
        else:
            self.balance[customer_name] -= amount
            self.customers[customer_name].append(f"Withdrawn: {amount}")
            print(f"Amount {amount} withdrawn successfully.")
            self.save_data()

    def initial_balance(self):
        customer_name = input("Enter customer name: ")
        print(f"Initial balance for {customer_name}: {self.balance.get(customer_name, 0)}")

    def bank_statement(self):
        customer_name = input("Enter customer name: ")
        print(f"Bank statement for {customer_name}:")
        for transaction in self.customers.get(customer_name, []):
            print(transaction)
        print(f"Current balance: {self.balance.get(customer_name, 0)}")

bank = Bank()

while True:
    print('1) Add Customer')
    print('2) Deposit Amount')
    print('3) Withdrawal Amount')
    print('4) Initial Balance')
    print('5) Bank Statement')
    print('6) Exit')

    choice = input("Enter your choice: ")

    if choice == '1':
        bank.add_customer()
    elif choice == '2':
        bank.deposit_amount()
    elif choice == '3':
        bank.withdrawal_amount()
    elif choice == '4':
        bank.initial_balance()
    elif choice == '5':
        bank.bank_statement()
    elif choice == '6':
        print("Exiting the program. Thank You for Visit Our Bank!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")