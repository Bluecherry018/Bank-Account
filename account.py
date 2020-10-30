from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, branch, account, balance):
        self._branch = branch
        self._account = account
        self._balance = balance

    @property
    def branch(self):
        return self._branch

    @property
    def account(self):
        return self._account

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount):
        if not isinstance(amount,(int, float)):
            raise ValueError("The amount needs to be numeric")
        self._balance = amount

    def deposit(self,amount):
        if not isinstance(amount,(int, float)):
            raise ValueError("The value for deposit needs to be numeric ")
        self.balance += amount
        self.details()

    def details(self):
        print(f'Branch: {self.branch}', end=' ')
        print(f'Account: {self.account}', end=' ')
        print(f'Balance: {self.balance}')

    @abstractmethod
    def withdraw(self, amount):
        pass

