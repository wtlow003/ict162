class MovieCard:
    def __init__(self, price):
        self._price = price
        self._tickets = 10 if price == 70 else 15       # assume price = 70 or 100 only

    @property
    def tickets(self):
        return self._tickets

    def redeem_ticket(self, qty=1):
        if qty > 2:
            raise ValueError("Maximum ticket redemptions is 2.")
        elif qty <= self._tickets:
            self._tickets -= qty
            return True
        return False

    def __str__(self):
        return f"Ticket price: ${self._price}, tickets remaining: {self._tickets}"


if __name__ == '__main__':
    mc1 = MovieCard(70)
    print(mc1)
    print(mc1.redeem_ticket(2))
    print(mc1)
    print(mc1.tickets)
