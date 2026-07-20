class Account:
    # Sarara gadii lama lama (__init__) ta'uu qaba
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance!")

    def statement(self):
        print(f"Account: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: {self.balance}")
        print("-" * 30)


class SavingsAccount(Account):
    def __init__(self, acc_no, name, balance, rate):
        # super().__init__ jedhamee sirreeffameera
        super().__init__(acc_no, name, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate / 100

    def statement(self):
        print("=== Savings Account ===")
        super().statement()


class CurrentAccount(Account):
    def __init__(self, acc_no, name, balance, overdraft):
        # super().__init__ jedhamee sirreeffameera
        super().__init__(acc_no, name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self.balance -= amount
        else:
            print("Overdraft limit exceeded!")

    def statement(self):
        print("=== Current Account ===")
        super().statement()


# Driver Code (Polymorphism)

a1 = SavingsAccount("1001", "Milki", 5000, 10)
a2 = CurrentAccount("1002", "Abebe", 3000, 2000)

a1.add_interest()
a2.withdraw(4500)

accounts = [a1, a2]

for account in accounts:
    account.statement()
