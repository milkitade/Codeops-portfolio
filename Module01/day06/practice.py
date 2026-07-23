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



# 1. SRP: Separate building, saving, and emailing into distinct classes
class Report:
    def __init__(self, text): self.text = text

class ReportSaver:
    def save(self, report): print(f"Saved: {report.text}")

class ReportEmailer:
    def send(self, report): print(f"Emailed: {report.text}")


# 2. OCP: Use a base class so adding shapes doesn't require modifying an if/elif tree
class Shape:
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h


# 3. SINGLETON: Force multiple instances to point to the exact same object
class AppSettings:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


# 4. FACTORY: Centralize object creation into one simple method call
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

class ShapeFactory:
    @staticmethod
    def create(kind, val):
        return Circle(val) if kind == "circle" else Rectangle(val, val)


# 5. OBSERVER: Broadcast updates dynamically to a list of subscribers
class NewsAgency:
    def __init__(self): self.subs = []
    def notify(self, msg): 
        for s in self.subs: print(f"Subscriber got: {msg}")


# --- RUN AND TEST EVERY STEP ---
if __name__ == "__main__":
    print("1. SRP:", end=" ")
    rep = Report("Data")
    ReportSaver().save(rep)

    print("2. OCP Area:", Rectangle(4, 5).area())

    print("3. Singleton Match?", AppSettings() is AppSettings())

    print("4. Factory Area:", ShapeFactory.create("circle", 3).area())

    print("5. Observer:")
    agency = NewsAgency()
    agency.subs.append("User1")
    agency.notify("NBE Update")
