from banking.BankAccount import BankAccount


account1 = BankAccount("123456789", 1000)
account2 = BankAccount("987654321", 500)

account1.deposit(200)
account2.withdraw(100)

print(f"Account 1 Balance: {account1.get_balance()}")
print(f"Account 2 Balance: {account2.get_balance()}")