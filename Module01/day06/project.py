# Observer
class SMSAlert:
    def update(self, message):
        print(f"SMS Alert: {message}")


# Account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        self.notify(f"{amount} deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.notify(f"{amount} withdrawn")
        else:
            print("Insufficient balance")


class SavingsAccount(Account):
    pass


class CurrentAccount(Account):
    pass


# Factory
class AccountFactory:
    @staticmethod
    def create(kind, owner, balance=0):
        if kind == "savings":
            return SavingsAccount(owner, balance)
        elif kind == "current":
            return CurrentAccount(owner, balance)
        else:
            raise ValueError("Unknown account type")



sms = SMSAlert()

account = AccountFactory.create("savings", "Abebe", 1000)

account.subscribe(sms)

account.deposit(500)
account.withdraw(300)