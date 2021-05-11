from abc import abstractmethod, ABC


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
    def name(self):
        return self._name

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

    @classmethod
    @abstractmethod
    def get_citizenship(cls):
        pass

    def __str__(self):
        return (f"Buyer Citizen: {type(self).get_citizenship()} "
                f"id: {self._buyer_id} "
                f"Name: {self._name} "
                f"Contact: {self._contact} "
                f"Number of properties: {self._number_of_properties}")


class SingaporeCitizen(Buyer):

    def __init__(self, buyer_id, name, contact, number_of_properties):
        super().__init__(buyer_id, name, contact, number_of_properties)

    def get_absd_rate(self):

        if self._number_of_properties == 2:
            rate = 0.12
        elif self._number_of_properties >= 3:
            rate = 0.15
        else:
            rate = 0.0

        return rate

    @classmethod
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
        self._transaction_id = type(self)._next_transaction_id
        type(self)._next_transaction_id += 1

    @property
    def buyer(self):
        return self._buyer

    @property
    def transacted_property(self):
        return self._transacted_property

    def buyer_id(self):
        return self._buyer.buyer_id

    def transaction_id(self):
        return self._transaction_id

    def absd_payable(self):
        return self._buyer.get_absd_rate() * self._transacted_property.property_value

    def bsd_payable(self):
        total_payable = 0.0
        property_value = self._transacted_property.property_value

        if property_value <= 180000:
            total_payable += 0.1 * property_value
        elif 180000 < property_value <= 360000:
            total_payable += (0.1 * 180000 + 0.2 * (property_value - 180000))
        elif 360000 < property_value <= 1000000:
            total_payable += (0.1 * 180000 + 0.2 * 180000 + 0.3 * (property_value - 360000))
        else:
            total_payable += (0.1 * 180000 + 0.2 * 180000 + 0.3 * 640000 + 0.4 * (property_value - 1_000_000))

        return total_payable

    def __str__(self):
        return (f"Transaction id: {self._transaction_id} ABSD: ${self.absd_payable():.2f} BSD: ${self.bsd_payable:.2f}\n"
                f"\tProperty Address: {self._transacted_property.address} Value: ${self.transacted_property.property_value:.0f}\n"
                f"\tBuyer Citizen: {self._buyer.get_citizenship()} id: {self._buyer.buyer_id} "
                f"Name: {self._buyer.name} Contact: {self._buyer.contact} Number of properties: {self._buyer.number_of_properties}")


if __name__ == "__main__":

    sc1 = SingaporeCitizen('T0001234X', 'Ann Chua', 92133123, 0)
    sc2 = SingaporeCitizen('T1234567F', 'Tom Teo', 98712123, 0)
    print(sc1, sc2, sep='\n')