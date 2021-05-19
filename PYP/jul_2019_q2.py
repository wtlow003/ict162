# Q2

class ExpenditureException(Exception):
    """Exception class for exception raised for Expenditure"""

    def __init__(self, message, error_type):
        self.error_type = error_type

    @property
    def error_type(self):
        return self._error_type


class Expenditure:
    """[summary]
    """

    def __init__(self, expenditure_date, amount, expenditure_type):
        self._expenditure_date = expenditure_date
        self._amount = amount
        self._expenditure_type = expenditure_type

    @property
    def expenditure_date(self):
        pass

    @property
    def amount(self):
        pass

    @property
    def expenditure_type(self):
        pass

    def __str__(self):
        return (f"${self._amount:.2f} "
                f"{self._expenditure_date} "
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
    pass