class BankAccount:
    def __init__(self, account_balance):
        self.__balance = account_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            print("Sorry! your funds are insufficient")
            return False

    def display_balance(self):
        print(f"\nyour available balanca is = ${self.__balance:.2f}")
