class Item:

    _standard_item_discount = 0.2

    def __init__(self, item_code: int, price: float):
        self._item_code = item_code
        self._price = price
        self._on_sales = False  # newly created, default to False

    @property
    def item_code(self):
        return self._item_code

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @property
    def on_sales(self):
        return self._on_sales

    @on_sales.setter
    def on_sales(self, new_on_sales):
        self._on_sales = new_on_sales

    def selling_price(self):
        return self._price * (1 - type(self)._standard_item_discount)

    def more_expensive(self, other_item):
        # True if item's price is more expensive than other_item's price
        return self._price > other_item.price

    @classmethod
    def get_standard_item_discount(cls):
        return cls._standard_item_discount

    @classmethod
    def set_standard_item_discount(cls, new_discount):
        cls._standard_item_discount = new_discount

    def __str__(self):
        return (f"Item code: {self._item_code} "
                f"OnSales: {self._on_sales} "
                f"Selling Price: ${(self.selling_price() if self._on_sales else self._price):.2f} "
                f"Normal Price: ${self._price:.2f}")


if __name__ == '__main__':
    i1 = Item(102, 3.55)
    i2 = Item(216, 2.00)

    print(i1, i2, sep='\n')

    if i1.on_sales:
        i1.on_sales = False
    else:
        i1.on_sales = True

    print(i1, i2, sep='\n')

    print(f"Is i2 more expensive than i1?: {i2.more_expensive(i1)}")

    # Reducing the standard discount by 0.05

    for item in [i1, i2]:
        item.set_standard_item_discount(item.get_standard_item_discount() - 0.05)

    print(i1.get_standard_item_discount(), i2.get_standard_item_discount(), sep='\n')
