"""
Design a `BankAccount` class using secure prefixing access modifiers to make account balance private
(`__balance`). Implement clean accessors utilizing the official `@property` and `@balance.setter`
decorators. Enforce custom business rules (e.g., balance updates cannot be negative numbers).
Sample Input: acc = BankAccount(100); acc.balance = -50
Expected Output: Raises: ValueError('Account balances cannot drop below absolute
zero.')
"""

class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Account balances cannot drop below absolute zero.")
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Account balances cannot drop below absolute zero.")
        self.__balance = amount


# Sample Input
acc = BankAccount(100)

try:
    acc.balance = -50
except ValueError as e:
    print(f"Raises: ValueError('{e}')")