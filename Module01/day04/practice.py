class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"'{self.title}' by {self.author}, {self.pages} pages")

# Create two books
book1 = Book("Python Programming", "John Smith", 300)
book2 = Book("Web Development", "David Lee", 250)

book1.describe()
book2.describe()
print("\n----------------------")

class Product:
    def __init__(self, name, price, quantity): # Fixed __init__ syntax
        self.name = name
        self.price = price
        self.__quantity = quantity # private attribute

    # Getter for quantity
    @property
    def quantity(self): 
        return self.__quantity

    # Setter for quantity
    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self.__quantity = value
        else:
            print("Quantity cannot be negative!")

    # Restock product
    def restock(self, n):
        self.__quantity += n

    # Sell product
    def sell(self, n):
        if n <= self.__quantity:
            self.__quantity -= n
        else:
            print("Not enough stock available!")

# 5. Prove independence
product1 = Product("Laptop", 50000, 10)
product2 = Product("Phone", 20000, 20)
product3 = Product("Tablet", 15000, 15)

print("Before selling:")
print(product1.name, product1.quantity)
print(product2.name, product2.quantity)
print(product3.name, product3.quantity)

# Change only product1
product1.sell(5)

print("\nAfter selling 5 laptops:")
print(product1.name, product1.quantity)
print(product2.name, product2.quantity)
print(product3.name, product3.quantity)

# Testing restock
product2.restock(10)
print("\nAfter restocking phones:")
print(product2.name, product2.quantity)

# Testing setter validation
product3.quantity = -5 
print(product3.name, product3.quantity)
