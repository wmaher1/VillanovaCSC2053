from bank_account import BankAccount

account = BankAccount("001798", 1000)
print(account)

account.deposit(120)
account.withdraw(200)
print(account)

account.get_balance()
print(account)
