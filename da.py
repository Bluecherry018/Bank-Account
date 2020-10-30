from account import Account

class DepositAccount (Account):
    def withdraw (self, amount):
        if self.balance < amount:
            print('Insufficient funds')
            return

        self.balance -= amount
        self.details()


