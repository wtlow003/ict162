# Q2
from datetime import datetime

class ExpenditureException(Exception):
    """Exception class for exception raised for Expenditure"""

    def __init__(self, message, error_type):
        super().__init__(message)
        self._error_type = error_type

    @property
    def error_type(self):
        return self._error_type


class Expenditure:
    """[summary]
    """

    def __init__(self, expenditure_date, amount, expenditure_type):
        self._expenditure_type = expenditure_type
        # initialising `_amount`
        if amount < 0:
            raise ExpenditureException(f"Amount ${amount} cannot be negative.", 'Amount')
        elif amount == 0:
            raise ExpenditureException(f"Amount cannot be zero.", 'Amount')
        else:
            self._amount = amount
        # initialising `_expenditure_date`
        if expenditure_date > datetime.now():
            formatted_date = expenditure_date.strftime('%a, %d %b %Y')
            raise ExpenditureException(f"{formatted_date} cannot be later than today.", 'Date')
        else:
            self._expenditure_date = expenditure_date

    @property
    def expenditure_date(self):
        return self._expenditure_date

    @property
    def amount(self):
        return self._amount

    @property
    def expenditure_type(self):
        return self._expenditure_type

    def __str__(self):
        return (f"${self._amount:.2f} "
                f"{self._expenditure_date.strftime('%a, %d %b %Y')} "
                f"{self._expenditure_type}")


class ExpenditureList:
    """[summary]
    """

    _types = ['Food', 'Transport', 'Education']

    def __init__(self):
        self._expenditures = []

    @classmethod
    def expenditure_types(cls):
        return cls._types

    def get_expenditures(self, expenditure_type, days):
        pass

    def get_expenditures_amount(self, expenditure_type, days):
        pass

    def add_expenditure(self, expenditure_date, amount, expenditure_type):
        pass

    def __str__(self):
        pass

if __name__ == '__main__':
    # testing Expenditure
    e1 = Expenditure(datetime(2019, 8, 14), 125, 'Food')
    e2 = Expenditure(datetime(2019, 8, 13), 4.50, 'Food')

    try:
        # testing raising errors in `Expenditure`
        e3 = Expenditure(datetime(2021, 8, 20), 300, 'Food')
    except ExpenditureException as e:
        print(f"{e.error_type} Error: {e}")

    # catch amount error - < 0
    try:
        e4 = Expenditure(datetime(2020, 5, 20), -10, 'Food')
    except ExpenditureException as e:
        print(f"{e.error_type} Error: {e}")

    # catch amount error - == 0
    try:
        e5 = Expenditure(datetime(2020, 5, 20), 0, 'Food')
    except ExpenditureException as e:
        print(f"{e.error_type} Error: {e}")

    print(e1, e2, sep='\n')