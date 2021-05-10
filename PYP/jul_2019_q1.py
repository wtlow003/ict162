from ABC import abstractmethod, ABC


class Buyer(ABC):

    def __init__(self, buyer_id, name, contact, number_of_properties):
        self._buyer_id = buyer_id
        self._name = name
        self._contact = contact
        self._number_of_properties = 0 + number_of_properties

    @property
    def buyer_id(self):
        return self._buyer_id

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, new_value):
        self._contact = new_value

    @property
    def number_of_properties(self):
        return self._number_of_properties

    @number_of_properties.setter
    def number_of_properties(self, new_value):
        self._number_of_properties = new_value

    @abstractmethod
    def get_absd_rate(self):
        pass

    @abstractmethod
    @classmethod
    def get_citizenship(cls):
        pass

    def __str__(self):
        return (f"Buyer Citizen: {type(self).get_citizenship()} "
                f"id: {self._buyer_id} "
                f"Name: {self._name} "
                f"Contact: {self._contact} "
                f"Number of properties: {self._number_of_properties}")


class SingaporeCitizen(Buyer):

    def __init__(self):
        super().__init__(buyer_id, name, contact, number_of_properties)

    def get_absd_rate(self):

        if self._number_of_properties == 2:
            rate = 0.12
        elif self._number_of_properties >= 3:
            rate = 0.15
        else:
            rate = 0.0

        return rate

    def get_citizenship(cls):
        return 'SC'


class TransactedProperty:

    def __init__(self, address, property_value):
        self._address = address
        self._property_value = property_value

    @property
    def address(self):
        return self._address

    @property
    def property_value(self):
        return self._property_value

    @property_value.setter
    def property_value(self, new_value):
        self._property_value = new_value

    def __str__(self):
        return f"Property Address: {self._address} Value: ${self._property_value:,.0f}"


class Transaction:

    _next_transaction_id = 1

    def __init__(self, transacted_property, buyer):
        self._transacted_property = transacted_property
        self._buyer = buyer
        self._absd_rate = buyer.get_absd_rate()
        self._transacted_property = self._next_transaction_id
        type(self)._next_transaction_id += 1