#variables
x = 5
y = 10
z = x + y
name = "Milki Tadesse"
age = 23
phone = +251922345674
print(z)
print(f'your name is {name} and your age is {age} and your phone number is {phone}')

#  type conversion 
age_text = input("Your age: ")   # e.g. "24" (a string!) 
age = int(age_text)              
# 24  (now an int) 
next_year = age + 1 
print(f'next year you will be {next_year} years old')

# conditional statements
mark = input("Enter mark :")
mark = int(mark)
if mark >= 90:
    print(" your mark is A+")
elif mark >= 85:
    print("your mark is A")
elif mark >= 80:
    print ("your mark is A-")
elif mark >= 75:
    print("your mark is B+")
elif mark >= 70:
    print("your mark is B")
elif mark >= 65:
    print("your mark is B-")
elif mark >= 70:
    print("your mark is C")
else:
    print("sorry, you are failed")

    # While and for loop
count = 1
while count <= 3:
    print("this number is ", count)
    count = count +1

for i in range(1, 3):
    print(i)

    name = ["Caalaa", "Obsaa", "keebeki", "Keebar"]
for nam in name:
    print(f"Maqaan kee ", nam)

    # function  Argument
def myfunction(fname, Mname, lname):
    print(f"your full name : {fname} {Mname} {lname}")

myfunction("caalaa", "obsaa","Beekaa")

def function(x):
    return x + 5
print(function(10))