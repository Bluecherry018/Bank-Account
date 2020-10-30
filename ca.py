from account import Account

class CurrentAccount (Account):
    def __init__(self, branch, account, balance, limit = 100):
        super().__init__(branch, account, balance)
        self._limit = limit

    @property
    def limit(self):
        return self._limit

    def withdraw(self, amount):
        if (self.balance + self.limit) < amount:
            print('Insufficient funds')
            return

        self.balance -= amount
        self.details()

