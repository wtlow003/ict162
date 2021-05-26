# LAB 3 Q2

class BankAccount:

    _interest_rate = 0.03

    def __init__(self, id, amount):
        self._account_id = id
        self._balance = amount

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @property
    def account_id(self):
        return self._account_id

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_amt):
        self._balance = new_amt

    def deposit(self, amount=20):
        self._balance += amount

    def withdraw(self, amount=20):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def transfer(self, other_acc, amount):
        if self.withdraw(amount):
            other_acc.deposit(amount)
            return True
        return False

    def accumulate_interest(self):
        self._balance += self._balance * type(self)._interest_rate

    def __str__(self):
        return f"{self._account_id} {self._balance:.2f}"


class JuniorAccount(BankAccount):

    # by refinement
    def __init__(self, id, guardian, amount):
        super().__init__(id, amount)
        self._guardian = guardian

    @property
    def guardian(self):
        return self._guardian

    # by refinement
    def withdraw(self, guardian, amount=20):
        if guardian == self._guardian and amount <= self._balance:
            self._balance -= amount
            return True
        return False

    # by replacement
    def accumulate_interest(self):
        self._balance += self._balance * (type(self).get_interest_rate() + 0.01)

    # by refinement
    def __str__(self):
        return f"Guardian: {self._guardian}, {super().__str__()}"


if __name__ == '__main__':
    a1 = BankAccount(1001, 5000)
    a2 = BankAccount(1002, 1000)
    print(a1.transfer(a2, 2500))
    print(a1.balance, a2.balance)
    # trying to exceed transfer amount
    print(a1.transfer(a2, 3000))
    print(a1.balance, a2.balance)
    # trying junior account ensuring that with guardian we can exceed alot more
    j1 = JuniorAccount(1003, 'John', 5000)
    print(j1.withdraw('Tom', 500))
    print(j1.balance)
    print(j1.withdraw('John', 500))
    print(j1.balance)