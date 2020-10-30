from deposit_account import DepositAccount
from current_account import CurrentAccount

deposit_account = DepositAccount(1111,2222,0)
deposit_account.deposit(10)
deposit_account.withdraw(5)

print('######################')

current_account = CurrentAccount(branch=1111,branch=333,balance=0,limit=500)
current_account.deposit(100)
current_account.withdraw(250)
current_account.withdraw(500)
current_account.deposit(1000)
