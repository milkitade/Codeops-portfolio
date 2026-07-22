
# unique cities
cities = ["Addis Ababa", "Jimma", "Adama", "Jimma", "Adama", "Hawassa"]

unique = set(cities)

print(unique)
print("Count:", len(unique))

# price report
grocery = {
    "Sugar": 120,
    "Rice": 180,
    "Oil": 350,
    "Soap": 90,
    "Salt": 30
}

for item, price in grocery.items():
    print(item, "-", price, "ETB")

    # Tax comprehension
prices = [100, 250, 400, 80]

tax_prices = [price * 1.15 for price in prices]

print(tax_prices)

# cheap items
prices = [100, 250, 400, 80]

cheap = [price for price in prices if price < 200]

print(cheap)

# read and write
with open("names.txt", "w") as file:
    file.write("Abebe\n")
    file.write("Kebede\n")
    file.write("Milki\n")

with open("names.txt", "r") as file:
    for name in file:
        print(name.strip())

        # try 
try:
    num = int(input("Enter a number: "))
    print("Result:", 1000 / num)

except ValueError:
    print("Invalid input! Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")