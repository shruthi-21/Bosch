# ---------------------------
# Base Class: BankAccount
# ---------------------------
class BankAccount:
    def __init__(self, name, acc_no, balance=0.0):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def getBalance(self):
        print("\nName    = ", self.name)
        print("Acc No  = ", self.acc_no)
        print("Balance = ", self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"{self.name} deposited ₹{amount}. New Balance = ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"{self.name}: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. New Balance = ₹{self.balance}")


# ---------------------------
# Savings Account
# ---------------------------
class SavingsAccount(BankAccount):
    def __init__(self, name, acc_no, balance=0.0, interest_rate=0.05):
        super().__init__(name, acc_no, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"{self.name}: Interest ₹{interest:.2f} applied. New Balance = ₹{self.balance}")


# ---------------------------
# Current Account
# ---------------------------
class CurrentAccount(BankAccount):
    def __init__(self, name, acc_no, balance=0.0, overdraft_limit=5000):
        super().__init__(name, acc_no, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance + self.overdraft_limit:
            print(f"{self.name}: Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. New Balance = ₹{self.balance}")


# ---------------------------
# Fixed Deposit Account
# ---------------------------
class FixedDepositAccount(BankAccount):
    def __init__(self, name, acc_no, balance=0.0, lock_in_period=6):
        super().__init__(name, acc_no, balance)
        self.lock_in_period = lock_in_period
        self.months_passed = 0

    def complete_month(self):
        self.months_passed += 1

    def withdraw(self, amount):
        if self.months_passed < self.lock_in_period:
            print(f"{self.name}: Cannot withdraw, lock-in period not over.")
        elif amount > self.balance:
            print(f"{self.name}: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. New Balance = ₹{self.balance}")


# ---------------------------
# Bank Class
# ---------------------------
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_no] = account

    def transfer_funds(self, from_acc_no, to_acc_no, amount):
        from_acc = self.accounts.get(from_acc_no)
        to_acc = self.accounts.get(to_acc_no)
        if not from_acc or not to_acc:
            print("Invalid account number.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        elif getattr(from_acc, 'overdraft_limit', 0) + from_acc.balance < amount:
            print(f"{from_acc.name}: Insufficient funds for transfer.")
        else:
            from_acc.balance -= amount
            to_acc.balance += amount
            print(f"₹{amount} transferred from {from_acc.name} to {to_acc.name}")


# ---------------------------
# --- Demonstration ---
# ---------------------------

bank = Bank()

# Create accounts with name "Shruthi"
savings = SavingsAccount("Shruthi", 101, 5000, 0.06)
current = CurrentAccount("Shruthi", 102, 2000, 3000)
fd = FixedDepositAccount("Shruthi", 103, 10000, 6)

# Add accounts to bank
bank.add_account(savings)
bank.add_account(current)
bank.add_account(fd)

# Savings account operations
savings.getBalance()
savings.deposit(2000)
savings.getBalance()
savings.withdraw(1000)
savings.getBalance()
savings.apply_interest()
savings.getBalance()

# Current account operations
current.getBalance()
current.withdraw(4000)  # overdraft allowed
current.getBalance()

# Fixed deposit operations
fd.getBalance()
fd.withdraw(2000)       # before lock-in
for _ in range(6):
    fd.complete_month()
fd.withdraw(2000)       # after lock-in
fd.getBalance()

# Fund transfer
bank.transfer_funds(101, 102, 3000)
savings.getBalance()
current.getBalance()
