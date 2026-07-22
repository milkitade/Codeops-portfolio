# temperature
temp = float(input("Enter Temperature in C: "))
if temp < 15:
    print("cold")
elif temp <= 28:
    print("warm")
else:
    print("hot")


# receipt  print using for loop
for receipt in range(1, 10):
    print(f"Receipt #{receipt} ")


# print even number by using loop and  module
for i in range(1,20):
    if i % 2 == 0:
        print(i)


# function 
def appliy_discount(price , precent=10):
    return price - (price * precent/ 100)
print(appliy_discount(100))
print(appliy_discount(100, 20))


#   countdown using while loop
count = 5
while count >= 1:
    print(count)
    count -= 1
    # print(count)

print("Liftoff")
    