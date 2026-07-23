class Account:
    def __init__(self, owner: str, account_number: str, balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance if balance >= 0 else 0.0

    # Read-only property for balance
    @property
    def balance(self) -> float:
        return self.__balance

    # Validated deposit method
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"[{self.owner}] Deposited {amount:,.2f} ETB.")
        else:
            print(f"[{self.owner}] Error: Deposit amount must be positive!")

    # Validated withdraw method
    def withdraw(self, amount: float):
        if amount <= 0:
            print(f"[{self.owner}] Error: Withdrawal amount must be positive!")
        elif amount > self.__balance:
            print(f"[{self.owner}] Error: Insufficient funds! Overdraft rejected.")
        else:
            self.__balance -= amount
            print(f"[{self.owner}] Withdrew {amount:,.2f} ETB.")

    # Bank statement method
    def statement(self):
        print(f"\n=== Addis Bank Statement ===")
        print(f"Owner:   {self.owner}")
        print(f"Account: {self.account_number}")
        print(f"Balance: {self.__balance:,.2f} ETB")
        print("=============================")


# --- Step 5: Create two accounts and run transactions ---
if __name__ == "__main__":
    print("--- Initializing Accounts ---")
    # Account 1 setup
    account1 = Account("Abebe Kebede", "AB-101", 10000.0)
    account1.statement()

    # Account 2 setup
    account2 = Account("Chaltu Alemu", "AB-102", 2500.0)
    account2.statement()

    print("\n--- Running Transactions ---")
    # Transactions for Abebe
    account1.withdraw(3000.0)
    account1.deposit(1500.0)
    account1.withdraw(12000.0) # Should fail (overdraft)

    # Transactions for Chaltu
    account2.deposit(5000.0)
    account2.withdraw(1000.0)
    account2.deposit(-200.0)   # Should fail (negative deposit)

    print("\n--- Final Statements ---")
    account1.statement()
    account2.statement()
