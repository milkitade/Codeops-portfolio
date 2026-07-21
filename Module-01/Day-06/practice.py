# SRP

class Report:
    def create(self):
        print("Creating report")

class ReportSaver:
    def save(self):
        print("Saving report")

# OCP
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

        # LSP 
class Bird:
    def move(self):
        print("Moving")

class Duck(Bird):
    def move(self):
        print("Flying")

bird = Duck()
bird.move()

# ISP
class Printer:
    def print_doc(self):
        print("Printing")

class Scanner:
    def scan_doc(self):
        print("Scanning")
# DIP
class Notifier:
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(message)

class Account:
    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self):
        self.notifier.send("Deposit successful")

email = EmailNotifier()
account = Account(email)
account.notify()