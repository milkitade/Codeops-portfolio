class Acc:
    def __init__(self, owner, account_number, balance):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

# Tarree herregoota uumaman keessatti kuusnu
accounts_list = []

while True:
    print("\n====== MENU ======")
    print("1. Create New Account")
    print("2. Exit")
    
    # Gidduu loopii keessatti gaafachuu qaba
    choice = input("Maal barbaadde? (1 ykn 2): ")

    if choice == "1":
        name = input("Please enter your name: ")
        account_number = input("Please enter your Account Number: ")
        balance = input("Please enter your balance: ")

        # Oobjektii uumuu
        Ac = Acc(name, account_number, balance)
        
        # List gubbaa jiru keessatti kuusuu
        accounts_list.append(Ac)
        print(f"Account uumameera: {Ac.owner} :{Ac.account_number} - {Ac.balance} Birr")

    elif choice == "2":
        print("Programichi cufameera!")
        break  # Loop sana dhaabuuf
        
    else:
        print("Maaloo 1 ykn 2 qofa filadhu!")
