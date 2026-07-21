class Account:
    def __init__(self, number, name, balance=0.0):
        self.number = number
        self.name = name
        self.balance = balance
        self.history = []  # Step 4: History stack

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))  # Push to stack

    def withdraw(self, amount):
        self.balance -= amount
        self.history.append(("withdraw", amount))  # Push to stack

    def undo_last(self):
        # Step 5: Undo using stack pop
        if self.history:
            action, amount = self.history.pop()
            if action == "deposit":
                self.balance -= amount
            elif action == "withdraw":
                self.balance += amount


class AccountRegistry:
    def __init__(self):
        self.accounts = {}  # Step 2: Dict for O(1) lookup

    def add(self, account):
        # Step 3: Add to dict - O(1)
        self.accounts[account.number] = account

    def find(self, number):
        # Step 3: Find from dict - O(1)
        return self.accounts.get(number)

    def list_all(self):
        # Step 3: Ordered list by account number
        return [self.accounts[num] for num in sorted(self.accounts.keys())]


# ==========================================
# AKKAATAA ITTI HOJJETU (OUTPUT ARGACHUUF)
# ==========================================

registry = AccountRegistry()

# 1. Herrega haaraa galmeessuu
acc1 = Account(102, "Chala", 500)
acc2 = Account(101, "Bonti", 1000)
registry.add(acc1)
registry.add(acc2)

# 2. Herrega tokko barbaadanii maallaqa itti naquu
my_acc = registry.find(102)
print(f"Maqaa: {my_acc.name}, Qarshii duree: {my_acc.balance}")

my_acc.deposit(200) 
print(f"Maallaqa itti naquu booda: {my_acc.balance}") # Output: 700

# 3. Undo gochuu (Hojii dhumaa haquu)
my_acc.undo_last()
print(f"Undo gochuu booda: {my_acc.balance}") # Output: 500 (Deebi'eera)

# 4. Herrega hunda tartiibaan tarreessuu
print("\n--- Tarreeffama Herregaa (Ordered List) ---")
for acc in registry.list_all():
    print(f"Lakk: {acc.number} | Maqaa: {acc.name} | Qarshii: {acc.balance}")
