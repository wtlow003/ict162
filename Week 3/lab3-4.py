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


class HSBCMovieCard(MovieCard):
    def __init__(self, price):
        super().__init__(price)
        self._tickets = 12 if price == 70 else 17

    def redeem_ticket(self, qty=1):
        if qty > 4:
            raise ValueError("Maximum ticket redemptions is 4.")
        elif qty <= self._tickets:
            self._tickets -= qty
            return True
        return False

    def __str__(self):
        return f"{type(self).__name__}, {super().__str__()}"


if __name__ == '__main__':
    mc1 = MovieCard(100)
    print(mc1)
    hmc1 = HSBCMovieCard(100)
    print(hmc1)
