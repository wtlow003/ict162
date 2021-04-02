class BankAccount:

    INTEREST_RATE = 0.03

    def __init__(self, id, amount: float = 20.00):
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

    def deposit(self, amount: float = 20.00):
        self._balance += amount

    def withdraw(self, amount: float = 20.00):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def transfer(self, other_account, amount):
        if self.withdraw(amount):
            other_account.balance += amount
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
    def withdraw(self, amount, guardian_name=None):
        # check for balance first superclass.withdraw() then check amount < 50
        if guardian_name == self._guardian:
            super().withdraw(amount)
            return True
        elif amount <= 50:
            super().withdraw(amount)
            return True
        return False

    # method overriding by replacement
    def accumulateInterest(self):
        self._balance += self._balance * (type(self).INTEREST_RATE + 0.01)
        return type(self), type(self).INTEREST_RATE

    def __str__(self):
        return super().__str__()


if __name__ == '__main__':
    b1 = BankAccount(101)
    b2 = BankAccount(102, 500)
    print(b1, b2)
    b2.transfer(b1, 100)
    print(b1, b2)
    j1 = JuniorAccount(103, 'Mary', 100)
    j2 = JuniorAccount(104, 'John', 500)
    print(j1, j2)
    print(j1.withdraw(60))
    print(j1.withdraw(100, 'Mary'))
    print(j1)
    b2.transfer(j1, 250)
    print(b2, j1)
