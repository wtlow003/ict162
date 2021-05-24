# LAB 3 Q1

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

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
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
    def withdraw(self, amount):
        if amount <= 50:
            return super().withdraw(amount)
        return False

    # by replacement
    def accumulate_interest(self):
        self._balance += self._balance * (type(self).get_interest_rate() + 0.01)

    # by refinement
    def __str__(self):
        return f"Guardian: {self._guardian}, {super().__str__()}"


if __name__ == '__main__':
    j = JuniorAccount(100, 'John', 500)
    # testing withdraw more than 50
    print(j.withdraw(100))
    # testing withdraw <= 50
    print(j.withdraw(50))
    print(j.balance)
    # testing deposit 100
    j.deposit(100)
    print(j.balance)
    # creating a normal account with same amount to compare accumulate interest
    b = BankAccount(101, 550)
    print(b.balance)
    # accumalating interest on both account
    j.accumulate_interest()
    b.accumulate_interest()
    # printing status
    print(j.balance, b.balance)
    print(j, b, sep='\n')