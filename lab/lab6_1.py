# LAB 6 QN 1-3
from abc import ABC, abstractmethod


# Q3
class InvalidCustomerException(Exception):
    """Raises exception in violation of business rule in Customer classes"""

# Q1
class Customer(ABC):

    _prevailing_interest = 0.025

    def __init__(self, id, name, loan):
        if (id[0] not in ['V', 'C']) and (not id[1:].isdigit()):
            raise InvalidCustomerException("Id does not conform to set rules.")
        else:
            self._id = id
        self._name = name
        if loan > self.get_credit_limit():
            raise InvalidCustomerException("Loan exceed credit limit")
        else:
            self._loan = loan

    @property
    def id(self):
        return self._id

    @property
    def loan(self):
        return self._loan

    @abstractmethod
    def get_credit_limit(self):
        pass

    @abstractmethod
    def get_interest_on_loan(self):
        pass

    def __str__(self):
        return f"{self._id} {self._name} {self._loan}"


class ValuedCustomer(Customer):

    def __init__(self, id, name, salary, loan):
        self._salary = salary
        super().__init__(id, name, loan)

    @property
    def salary(self):
        return self._salary

    def get_credit_limit(self):
        return self._salary * 12 * 2.5

    def get_interest_on_loan(self):
        return self._loan * (type(self)._prevailing_interest + 0.01)

    def __str__(self):
        return f"{self._id} {self._name} {self._salary} {self._loan}"


class CorporateCustomer(Customer):

    def __init__(self, id, name, loan, business, asset_value):
        self._business = business
        self._asset_value = asset_value
        super().__init__(id, name, loan)


    @property
    def business(self):
        return self._business

    @property
    def asset_value(self):
        return self._asset_value

    def get_credit_limit(self):
        return self._asset_value * 3

    def get_interest_on_loan(self):
        return self._loan * (type(self)._prevailing_interest + 0.005)

    def __str__(self):
        return f"{super().__str__()} {self._business} {self._asset_value}"

# Q2
class CustomerList:

    def __init__(self):
        self._customers = []

    def add(self, customer):
        if customer not in self._customers:
            self._customers.append(customer)

    def search(self, id):
        for cust in self._customers:
            if cust.id == id:
                return cust
        return None

    def list_all(self):
        return ''.join(
            f"\n{cust} {cust.get_credit_limit()} {cust.get_interest_on_loan()}"
            for cust in self._customers
        )


if __name__ == '__main__':
    try:
        c1 = ValuedCustomer('V100', 'Jensen', 3500, 10000)
        c2 = CorporateCustomer('V101', 'Pencils Inc.', 100000, 'Stationary', 50000)
        c3 = ValuedCustomer('V102', 'John', 5000, 25000)
        # adding three customers into the list
        cl = CustomerList()
        cl.add(c1)
        cl.add(c2)
        cl.add(c3)
        # show all the customers
        print(cl.list_all())
    except InvalidCustomerException as e:
        print(e)