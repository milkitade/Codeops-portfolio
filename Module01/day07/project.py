class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance


accounts = []

while True:
    print("\n===== Account Menu =====")
    print("1. Add Account")
    print("2. Search Account")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        account_number = input("Enter Account Number: ")
        balance = float(input("Enter Balance: "))

        acc = Account(name, account_number, balance)
        accounts.append(acc)

        print("Account Added Successfully!")

    elif choice == "2":
        search = input("Enter Account Number: ")

        found = False
        for acc in accounts:
            if acc.account_number == search:
                print("\n----- Account Information -----")
                print("Name:", acc.name)
                print("Account Number:", acc.account_number)
                print("Balance:", acc.balance)
                found = True
                break

        if not found:
            print("Account Not Found!")

    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("ivalid choice")


        
def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i  # Found! Returns the index ()
    return -1  # Not found



num_list = [5, 3, 8, 2, 9]
target = 8

print(linear_search(num_list, target))  # Output: 2


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == target:
            return mid  # Found!
        elif sorted_list[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half

    return -1  # Not found



ordered_list = [2, 3, 5, 8, 9]  # Must be sorted!
target = 8

print(binary_search(ordered_list, target))  # Output: 3
