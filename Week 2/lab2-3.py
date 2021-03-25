class Product:
    def __init__(self, product_code: str, description: str, unit_price: float):
        self._product_code = product_code
        self._description = description
        self._unit_price = unit_price

    @property
    def product_code(self):
        return self._product_code

    @property
    def description(self):
        return self._description

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, new_price):
        self._unit_price = new_price

    def __str__(self):
        return f"{self._product_code} {self._description} {self._unit_price}"


class CartItem:
    def __init__(self, product: Product, quantity: int):
        self._product = product
        self._quantity = quantity
        # key:val, product_code:product_cost * quantity for easy retrieval
        self._cost = product.unit_price * quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @property
    def cost(self):
        return self._cost

    def __str__(self):
        return f"{self._product} {self._quantity} {self._cost}"

class ShoppingCart:
    def __init__(self, customer_name: str):
        self._customer_name = customer_name
        self._cart_items = []

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def cart_item(self):
        return self._cart_items


    def search_in_cart(self, product_code):
        for c in self._cart_items:
            if c.product.product_code == product_code:
                return c

    def add_to_cart(self, new_cart_item: CartItem):
        self._cart_items.append(new_cart_item)

    def remove_from_cart(self, product_code: str):
        c = self.search_in_cart(product_code)
        if c is None:
            return False
        else:
            self._cart_items = [c for c in self._cart_items if c.product.product_code != product_code]
        return True

    def total_cost(self):
        return sum([c.cost for c in self._cart_items])

    def cart_str(self):
        return '\n'.join([str(c) for c in self._cart_items])

    def __str__(self):
        return f"{self.customer_name} \n{self.cart_str()} \n{self.total_cost()}"

if __name__ == '__main__':
    p1 = Product('1', "A bar of Hershey's Chocolate", 4.99)
    p2 = Product('2', "Fuji Apple", 0.99)
    p3 = Product('3', 'Dettol Handwash', 8.99)
    p4 = Product('4', 'Raw Salmon', 5.49)
    print(p1, p2, p3, p4, sep='\n')
    print('\n')
    # include 2 quantity of hersheys
    c1 = CartItem(p1, 2)
    c2 = CartItem(p2, 4)
    c3 = CartItem(p3, 1)
    c4 = CartItem(p4, 5)
    print(c1, c2, c3, c4, sep='\n')
    print('\n')
    s1 = ShoppingCart('Jensen')
    s1.add_to_cart(c1)
    s1.add_to_cart(c2)
    s1.remove_from_cart('1')
    s1.add_to_cart(c1)
    s1.add_to_cart(c3)
    s1.add_to_cart(c4)
    print(s1)
    print('\n')
    # search for a particular product
    print(s1.search_in_cart('1'))
    print(s1.search_in_cart('2'))
    print(s1.search_in_cart('3'))
    print(s1.search_in_cart('4'))
    print(s1.search_in_cart('5'))
