class BankAccount:
    def __init__(self, account_id, pin, balance=100):
        self._account_id = account_id
        self._pin = pin
        self._balance = balance

    '''Getter method for account_id, pin, balance, Setter method for pin, balance'''
    @property
    def account_id(self):
        return self._account_id

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    @pin.setter
    def pin(self, new_pin):
        self._pin = new_pin

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def change_pin(self, old_pin, new_pin):
        '''Method to change pin only if old_pin matches existing pin'''
        if old_pin == self._pin:
            self._pin = new_pin
            return True
        else:
            return False

    def deposit(self, amount):
        '''Method add amount to the balance'''
        self._balance += amount

    def withdraw(self, amount):
        '''Method to withdraw amount from the balance'''
        if amount < self._balance:
            self._balance -= amount
            return True
        else:
            return False

    def transfer(self, bank_account, amount):
        '''Method to transfer from one account to another bank account'''
        if amount < self._balance:
            self._balance -= amount
            bank_account.deposit(amount)
            return True
        else:
            return False

    def __str__(self):
        return f"{self._account_id} {self._balance}"


if __name__ == '__main__':
    b1 = BankAccount('B1', pin=111)
    print(b1.deposit(100))
    print(b1.balance)
    # changing the pin for 'B1'
    if b1.change_pin(101, 105):
        print("Pin changed successfully!")
    else:
        print("Incorrect pin given, pin unchanged.")
    print(b1.change_pin(101, 105))     # inputting wrong pin
    print(b1.change_pin(111, 105))     # inputting correct pin
    b2 = BankAccount('B2', pin=100)
    # withdrawing 200 => more than balance, return False
    print(b2.withdraw(200))
    # transfering $100 from B1 to B2
    print(b1.transfer(b2, 100))
    print(b1.balance, b2.balance)
