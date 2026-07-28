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

# dictionery 
person = {
    "name":"milki",
    "age" : "24",
}
print(person)




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





