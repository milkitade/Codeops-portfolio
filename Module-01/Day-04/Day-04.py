# OOP , class , object, constructer,and encapsulation


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
maqa = Person("milki", 22)
print(maqa.name, maqa.age)


class Account:
    def init(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        """Return the account balance (read-only)."""
        return self.__balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        self.__balance += amount
        print(f"Successfully deposited {amount} Birr.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return

        if amount > self.__balance:
            print("Error: Insufficient balance.")
            return

        self.__balance -= amount
        print(f"Successfully withdrew {amount} Birr.")

    def display_account(self):
        """Display account information."""
        print("\n----------------------------")
        print(f"Owner          : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : {self.balance} Birr")
        print("----------------------------")


# ----------------------------
# Testing the Account Class
# ----------------------------

account1 = Account("Milki Tadesse", "ACC1001", 5000)
account2 = Account("Abdi Ali", "ACC1002", 3000)

# Transactions
account1.deposit(1500)
account1.withdraw(2000)

account2.deposit(700)
account2.withdraw(5000)   # Insufficient balance
account2.deposit(-200)    # Invalid deposit

# Display final account information
account1.display_account()
account2.display_account()