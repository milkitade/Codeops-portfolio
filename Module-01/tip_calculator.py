#varabiles
total_bill = 2000 
people = 5
tip_rate = 0.10
   
#function 
def split_bill(total_bill, people,tip_rate):
    tip = total_bill * tip_rate  #200
    total_with_tip = total_bill + tip #2000 + 200 = 2200
    share = total_with_tip / people
    return share 

#function call
share = split_bill(total_bill, people, tip_rate)

#list of people
list_of_people = ["Chala", "Sena", "Chaltu", "Jora", "Bona"]

print("TeleBirr Tip Calculator")
print(f"Total  bill: {total_bill} ETB")
print(f"Number of People: {people}")
print(f"Tip rate: {tip_rate * 100}%")
 
 #For loop
for list in list_of_people:
    print(f"{list} Your share is : {share} ETB")
