# bank_account.py

class BankAccount:
    def __init__(self, account_balance=0):
        self.__balance = account_balance  # Encapsulated private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        elif amount < 0:
            print("Insufficient funds or invalid amount.")
        else:
            print("Insufficient funds.")
            return False
# Insufficient funds or invalid amount.
# Insufficient funds.

    def display_balance(self):
        print(f"Current Balance:{self.__balance}")
