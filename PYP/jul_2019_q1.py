from abc import abstractmethod, ABC


class Buyer(ABC):

    def __init__(self, buyer_id, name, contact, number_of_properties):
        self._buyer_id = buyer_id
        self._name = name
        self._contact = contact
        self._number_of_properties = 0

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

    def get_absd_rate(self):
        rate = 0.0
        if self._number_of_properties + 1 == 2:
            rate = 0.12
        elif self._number_of_properties + 1 >= 3:
            rate = 0.15

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
        # Increasing the buyer's properties count
        buyer.number_of_properties += 1

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
        return self._absd_rate * self._transacted_property.property_value

    def bsd_payable(self):
        total_payable = 0.0
        property_value = self._transacted_property.property_value

        if property_value <= 180000:
            total_payable += 0.01 * property_value
        elif 180000 < property_value <= 360000:
            total_payable += (0.01 * 180000 + 0.02 * (property_value - 180000))
        elif 360000 < property_value <= 1000000:
            total_payable += (0.01 * 180000 + 0.02 * 180000 +
                              0.03 * (property_value - 360000))
        else:
            total_payable += (0.01 * 180000 + 0.02 * 180000 +
                              0.03 * 640000 + 0.04 * (property_value - 1_000_000))

        return total_payable

    def __str__(self):
        return (f"Transaction id: {self._transaction_id} ABSD: ${self.absd_payable()} BSD: ${self.bsd_payable():.2f}\n"
                f"\tProperty Address: {self._transacted_property.address} "
                f"Value: ${self.transacted_property.property_value:.0f}\n"
                f"\tBuyer Citizen: {self._buyer.get_citizenship()} "
                f"id: {self._buyer.buyer_id} "
                f"Name: {self._buyer.name} "
                f"Contact: {self._buyer.contact} "
                f"Number of properties: {self._buyer.number_of_properties}")


class Registry:

    def __init__(self):
        self._transactions = []
        self._buyers = []

    def register_buyer(self, buyer):
        buyer_ids = [buyer.buyer_id for buyer in self._buyers]
        if buyer.buyer_id not in buyer_ids:
            self._buyers.append(buyer)
            return True
        return False

    def locate_buyer(self, buyer_id):
        for buyer in self._buyers:
            if buyer_id == buyer.buyer_id:
                return buyer
        return None

    def remove_buyer(self, buyer_id):
        for buyer in self._buyers:
            if buyer_id == buyer.buyer_id and buyer.number_of_properties == 0:
                self._buyers.remove(buyer)
                return True
        return False

    def locate_transaction(self, transaction_id):
        for transaction in self._transactions:
            if transaction_id == transaction.transaction_id:
                return transaction
        return None

    def add_transaction(self, transaction):
        transaction_ids = [transc.transaction_id for transc in self._transactions]
        if transaction.transaction_id not in transaction_ids:
            self._transactions.append(transaction)
            return True
        return False

    def transaction_str(self):
        if self._transactions:
            transactions = '\n'.join([str(transc) for transc in self._transactions])
            return transactions
        else:
            return "No transaction in registry"

    def buyer_str(self):
        if self._buyers:
            buyers = '\n'.join([str(buyer) for buyer in self._buyers])
            return buyers
        else:
            return "No buyers in registry"

    def __str__(self):
        return (f"Buyer list:\n{self.buyer_str()}\n"
                f"\nTransaction list:\n{self.transaction_str()}")


if __name__ == "__main__":

    sc1 = SingaporeCitizen('T0001234X', 'Ann Chua', 92133123, 0)
    sc2 = SingaporeCitizen('T1234567F', 'Tom Teo', 98712123, 0)
    # print(sc1, sc2, sep='\n')
    p1 = TransactedProperty('12 Tampines Road', 1_500_000)
    t1 = Transaction(p1, sc2)
    # print(p1)
    # print(t1)
    r = Registry()
    # Adding two buyers
    r.register_buyer(sc1)
    r.register_buyer(sc2)
    r.add_transaction(t1)
    p2 = TransactedProperty('14 Tampines Road', 1_500_000)
    t2 = Transaction(p2, sc2)
    r.add_transaction(t2)
    # registering another buyer
    sc3 = SingaporeCitizen('T000898U', 'Ismail B', 92888866, 0)
    # adding new transacted property
    p3 = TransactedProperty('16 Tampines Road', 1_800_000)
    # adding transaction
    t3 = Transaction(p3, sc3)
    # adding transaction into the registry
    r.add_transaction(t3)
    print(r)