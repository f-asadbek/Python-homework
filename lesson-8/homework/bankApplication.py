class Account:
    def __init__(self, account_number, name, balance = 0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.account_number}, {self.name}, {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, account_number, name, initial_deposit):
        try:
            if account_number in self.accounts:
                raise ValueError("The account number already exists!")
            self.accounts[account_number] = Account(account_number, name, initial_deposit)
            self.save_to_file()
            print(f"Account created successfully! Account number: {account_number}")
        except ValueError:
            print("Error!")

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(f"Account number: {account.account_number}, Name: {account.name}, Balance: {account.balance}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number].balance += amount
            self.save_to_file()
            print(f"Amount deposited successfully! Account balance: {self.accounts[account_number].balance}")
        else:
            print("Invalid operation!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and 0 < amount <= self.accounts[account_number].balance:
            self.accounts[account_number].balance -= amount
            self.save_to_file()
            print(f"Amount withdrawn successfully! Account balance: {self.accounts[account_number].balance}")
        else:
            print("Invalid operation!")

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for account in self.accounts.values():
                file.write(account.__str__() + "\n")

    def load_from_file(self):
        with open("accounts.txt", "w") as file:
            file.write('')
        with open("accounts.txt", "r") as file:
            for line in file:
                account_number, name, balance = line.strip().split(",")
                self.accounts[account_number] = Account(account_number, name, float(balance))

if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\n1. Create Account\n2. View Account\n3. Deposit Money\n4. Withdraw Money\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(acc_num, name, initial_deposit)
        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.view_account(acc_num)
        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")
