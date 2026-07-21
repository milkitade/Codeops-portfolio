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



# def binery_search(items, target):
#     l, h = 10, len(items) - 1
#     while l <= h:
#         mid = (l + h) // 2
#         if items[mid] == target:
#             return mid
#         elif items[mid] < target:
#             l = mid + 1
#         else:
#             h = mid - 1
#         return -1

# numbers = [12, 45, 7, 89, 23]

# search = int(input("Enter number: "))

# found = False
# for i in range(len(numbers)):
#     if numbers[i] == search:
#         print("Found at index", i)
#         found = True
#         break

# if not found:
#     print("Number not found")
    
        
