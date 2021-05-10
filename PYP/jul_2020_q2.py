from datetime import datetime
from jul_2020_q1 import Item


class PurchaseItem():

    def __init__(self, item, quantity):
        self._item = item
        self._quantity = quantity
        self._purchase_price = float(item.price)

    @property
    def purchase_price(self):
        return self._purchase_price

    @property
    def item(self):
        return self._item

    def item_code(self):
        return self._item.item_code

    def sub_total(self):
        return self.purchase_price * self._quantity

    def __str__(self):
        return (f"{self._item}\n"
                f"Purchased price: ${self._purchase_price} "
                f"Quantity: {self._quantity} "
                f"Subtotal: ${self.sub_total()}")

class Purchase:

    _next_purchase_id = 1

    def __init__(self):
        self._purchase_id = type(self)._next_purchase_id
        self._purchase_date = datetime.now()
        self._purchase_items_list = []
        type(self)._next_purchase_id += 1

    @property
    def purchase_date(self):
        return self._purchase_date

    def days_from_purchase(self):
        return (self._purchase_date - datetime.now()).days

    def add_purchase_item(self, purchase_item):
        item_codes = [p_item.item.item_code for p_item in self._purchase_items_list]

        if purchase_item.item.item_code not in item_codes:
            self._purchase_items_list.append(purchase_item)
            return True
        return False

    def remove_purchase_item(self, item_code):

        removed = False
        for idx, p_item in enumerate(self._purchase_items_list):
            if p_item.item.item_code == item_code:
                self._purchase_items_list.pop(idx)
                removed = True
        return removed

    def grand_total(self):
        total_sum = 0.0

        for p_item in self._purchase_items_list:
            total_sum += p_item.sub_total()

        return total_sum

if __name__ == '__main__':
    # Q2d(i)
    i1 = Item(102, 3.55)
    pi = PurchaseItem(i1, 2)
    print(pi)

    # Q2d(ii)
    p = Purchase()
    p.add_purchase_item(pi)
    print(p.grand_total())