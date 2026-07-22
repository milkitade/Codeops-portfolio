# # OOP , class , object, constructer,and encapsulation


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
maqa = Person("milki", 22)
print(maqa.name, maqa.age)


# create a class and object
# Account creation 

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def NewAcc(self, acc):
        self.balance += acc
        print(f" Dear {self.owner} your account is Successfully created with : {self.balance} ETB")
    def NewAc(self, bcc):
        self.balance += bcc
        print(f" Dear {self.owner} your account is Successfully created with : {self.balance} ETB")

Cus1 = Account("Sabaaf", 50)
Cus1.NewAcc(20)
Cus2 = Account("Obsaa", 50)
Cus2.NewAc(10)



# Encapsulation concept,,, encapsulation means the process of protecting data internal class

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
