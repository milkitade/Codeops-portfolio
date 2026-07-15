# python collection , list, Tuple, set, Dictionary

#list 
cities = ["Finfinnee", "Amboo", "Jimmaa", "Wollega"]

cities.insert(1,"Dire Dewa")
cities.append("Adamaa")
cities.sort()
print(cities)


# Tuple

people = ("kena","Bona","cala", "kena")
print(people)



# # reading files
# with open("customer.txt") as f:
#     for line in f:
#         print(line.strip())




# transaction_report.py

# transactions = {}

# try:
#     # Read the transaction file
#     with open("transactions.txt", "r") as file:
#         for line in file:
#             line = line.strip()

#             if not line:
#                 continue

#             name, amount = line.split(",")
#             amount = float(amount)

#             if name in transactions:
#                 transactions[name] += amount
#             else:
#                 transactions[name] = amount

#     # Sort by highest total spend
#     sorted_transactions = sorted(
#         transactions.items(),
#         key=lambda x: x[1],
#         reverse=True
#     )

#     print("=== Transaction Report ===")

#     # Write the report to a file
#     with open("report.txt", "w") as report:
#         for name, total in sorted_transactions:
#             output = f"{name}: {total:.2f}"
#             print(output)
#             report.write(output + "\n")

#     print("\nReport saved to report.txt")

# except FileNotFoundError:
#     print("Error: transactions.txt file not found.")


    # Module and imports

# we can use module in 4 ways like import whole module,, import specific attribute ,,,Import with an Alias,,,
#  Import Specific Attributes with an Alias

# import whole module
import math

print(math.sqrt(25))

# import specific attribute
from math import pi, sqrt
print(sqrt(16))
print(pi)

# import with an alias 

import random as rdm

print(rdm.randrange(1, 10))

#  Import Specific Attributes with an Alias
from os.path import join as join_path

print(join_path("folder", "file.txt"))
