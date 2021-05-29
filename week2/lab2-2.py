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
        if amount <= self._balance:
            self._balance -= amount
            bank_account.deposit(amount)
            return True
        else:
            return False

    def __str__(self):
        return f"{self._account_id} {self._balance}"


class Bank:
    def __init__(self, bank_name: str):
        self._bank_name = bank_name
        self._bank_accounts = {}

    # Getter property for bank_name
    @property
    def bank_name(self):
        return self._bank_name

    def add(self, account):
        '''Method to add a bank account to the bank'''
        if account.account_id not in self._bank_accounts:
            self._bank_accounts[account.account_id] = account
            return True
        else:
            return False

    def search(self, account_id):
        '''Method to search and return a bank account based on account_id'''
        if account_id in self._bank_accounts:
            return self._bank_accounts[account_id]
        else:
            return None

    def remove(self, account_id):
        '''Method to search and remove a bank account based on acount_id'''
        if account_id in self._bank_accounts:
            del self._bank_accounts[account_id]
            return True
        else:
            return False

    def transfer(self, first_account_id, second_account_id, amount):
        '''Method to transfer between two account, both account must exist first'''
        if first_account_id in self._bank_accounts and second_account_id in self._bank_accounts:
            account_to = self._bank_accounts[first_account_id]
            account_from = self._bank_accounts[second_account_id]
            return account_to.transfer(account_from, amount)
        else:
            return False

    def list_all(self):
        '''Method to print all bank account, summary line of total account for all customers'''
        accounts = '\n'.join(f'{acc[1].account_id} {acc[1].balance}' for acc in self._bank_accounts.items())
        total_balance = sum([acc[1].balance for acc in self._bank_accounts.items()])
        summary = f"Total account balance in {self._bank_name}: ${total_balance}"
        return accounts + '\n' + summary

    def __str__(self):
        return f"{self._bank_name} {self._bank_accounts}"

if __name__ == '__main__':
    def menu():
        print("Menu")
        print("1.   Open Bank Account")
        print("2.   Check Balance")
        print("3.   Transfer Money")
        print("4.   Close Account")
        print("5.   List all accounts")
        print("6.   Quit.")

    def main():
        bank = Bank('ABC')
        while True:
            # display menu
            menu()
            # obtain user inputs
            choice = int(input("\nEnter your menu option: "))
            if choice <= 0 or choice > 6:
                print("Invalid option! Please enter your menu option.")
            elif choice == 1:
                id_choice = int(input("Please enter your bank account id: "))
                pin_choice = int(input("Please enter your desired bank account pin of 4 digits: "))
                bal_choice = input("Please enter your initial deposit, if left empty, initial balance is set at $100: ")
                if len(bal_choice) != 0:
                    bank_account = BankAccount(id_choice, pin_choice, int(bal_choice))
                else:
                    bank_account = BankAccount(id_choice, pin_choice)
                # adding account to the bank
                bank.add(bank_account)
            elif choice == 2:
                account_id = int(input('Enter your account id: '))
                account_pin = int(input('Enter your account pin: '))
                account = bank.search(account_id)
                if account_pin == account.pin:
                    print(f"The account balance is: ${account.balance}")
            elif choice == 3:
                account_to = int(input("Enter the account to retrieve the funds from: "))
                account_from = int(input("Enter the account to deposit the funds to: "))
                amount = int(input("Enter the amount to transfer: "))
                bank.transfer(account_to, account_from, amount)
            elif choice == 4:
                account_del = int(input("Enter the account to delete: "))
                print(bank.remove(account_del))
            elif choice == 5:
                print('\n')
                print(bank.list_all())
            elif choice == 6:
                break

    main()
