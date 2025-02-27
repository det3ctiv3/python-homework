import os
import random


class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account #{self.account_number} | Name: {self.name} | Balance: ${self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit can’t be negative, you cheapskate.")
            return
        account_number = random.randint(10000, 99999)  # Simple unique-ish number
        while account_number in self.accounts:
            account_number = random.randint(10000, 99999)  # Keep it unique
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        print(f"Account created: {new_account}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print(f"Account #{account_number} doesn’t exist. Try harder.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print(f"Account #{account_number} not found. Stop dreaming.")
            return
        if amount <= 0:
            print("Deposit amount must be positive, genius.")
            return
        account.balance += amount
        self.save_to_file()
        print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print(f"Account #{account_number} not found. Nice try.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive, slick.")
            return
        if amount > account.balance:
            print(f"Not enough cash, broke-ass. Balance: ${account.balance:.2f}")
            return
        account.balance -= amount
        self.save_to_file()
        print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")

    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            for account in self.accounts.values():
                f.write(f"{account.account_number},{account.name},{account.balance}\n")

    def load_from_file(self):
        if not os.path.exists("accounts.txt"):
            return  # No file, no problem—start fresh
        try:
            with open("accounts.txt", "r") as f:
                for line in f:
                    if line.strip():  # Skip empty lines
                        number, name, balance = line.strip().split(",")
                        self.accounts[int(number)] = Account(int(number), name, float(balance))
        except Exception as e:
            print(f"File load failed: {e}. Starting with an empty bank.")


def main():
    bank = Bank()
    while True:
        print("\n--- Bank Menu ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")
        choice = input("Pick an option (1-5): ")

        if choice == "1":
            name = input("Enter your name: ")
            try:
                deposit = float(input("Enter initial deposit: "))
                bank.create_account(name, deposit)
            except ValueError:
                print("That’s not a number, dumbass.")

        elif choice == "2":
            try:
                number = int(input("Enter account number: "))
                bank.view_account(number)
            except ValueError:
                print("Account number’s gotta be digits, not doodles.")

        elif choice == "3":
            try:
                number = int(input("Enter account number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(number, amount)
            except ValueError:
                print("Numbers only, no funny business.")

        elif choice == "4":
            try:
                number = int(input("Enter account number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(number, amount)
            except ValueError:
                print("Stick to numbers, not nonsense.")

        elif choice == "5":
            print("Later, moneybags.")
            break

        else:
            print("Pick 1-5, or get lost.")


if __name__ == "__main__":
    main()