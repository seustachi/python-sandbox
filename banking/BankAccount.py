class BankAccount:

    total_accounts = 0
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"BankAccount(account_number={self.account_number}, balance={self.balance})"