class BankAccount:

    INTEREST_RATE = 0.03

    def __init__(self, id, amount):
        self._accountId = id
        self._balance = amount

    @property
    def accountId(self):
        return self._accountId

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amt):
        self._balance = amt

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def accumulateInterest(self):
        self._balance += self._balance * type(self).INTEREST_RATE

    def __str__(self):
        return '{} {:.2f}'.format(self._accountId, self._balance)


class JuniorAccount(BankAccount):

    def __init__(self, id, guardian, amount):
        super().__init__(id, amount)
        self._guardian = guardian

    @property
    def guardian(self):
        return self._guardian

    @guardian.setter
    def guardian(self, new_guardian):
        self._guardian = new_guardian

    # method overriding by refinement
    def withdraw(self, amount):
        # check for balance first superclass.withdraw() then check amount < 50
        if amount <= 50:
            super().withdraw(amount)

    # method overriding by replacement
    def accumulateInterest(self):
        self._balance += self._balance * (type(self).INTEREST_RATE + 0.01)
        return type(self), type(self).INTEREST_RATE

    def __str__(self):
        return super().__str__()


if __name__ == '__main__':
    j1 = JuniorAccount(101, 'Max', 1000)
    print(j1)
    print(type(j1))
    print(j1.accumulateInterest())
    print(j1)
    print(j1.withdraw(100))
    print(j1)
    print(j1.withdraw(50))
    print(j1)
    print(j1.accumulateInterest())
    print(j1)
