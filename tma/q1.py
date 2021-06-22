from datetime import datetime, timedelta


# Q1(a)
class Customer:
    """A class to represent a customer.

    Example:
        >>> customer = Customer('Peter', 99998888)

    """

    def __init__(self, name, contact):
        """Constructs and initialises all necessary attributes for the
        Customer object.

        The `__init__` method initialises two attributes.

        Args:
            name (str): The name of the customer.
            contact (str): The contact number of the customer.

        """

        self._name = name
        self._contact = str(contact)

    @property
    def name(self):
        """The name of the customer.

        :getter: Return the Customer object's name.
        :rtype: str

        """

        return self._name

    @property
    def contact(self):
        """The contact of the customer.

        :getter: Return the Customer object's contact.
        :setter: Set the existing contact with `new_contact` (str).
        :rtype: str

        """

        return self._contact

    @contact.setter
    def contact(self, new_contact):
        self._contact = str(new_contact)

    def __str__(self):
        return f"{self._name} {self._contact}"


# Q1(b)
class Staycation:
    """A class to represent a staycation information (e.g. Hotel)

    """

    def __init__(self, hotel_name, nights, cost, voucher_allowed=True):
        """Constructs and initialises all necessary attributes for the
        Staycation object.

        The `__init__` method initialises four attributes.

        Args:
            hotel_name (str):  The name of the staycation hotel.
            nights (int): The number of nights booked for the staycation.
            cost (float): The cost of the staycation per night.
            voucher_allowed (bool): Whether voucher usage is allowed,
                default to [True].

        """
        self._hotel_name = hotel_name
        self._nights = int(nights)
        self._cost = float(cost)
        self._voucher_allowed = voucher_allowed

    @property
    def hotel_name(self):
        """The staycation hotel name.

        :getter: Return the staycation hotel's name
        :rtype: str

        """

        return self._hotel_name

    @property
    def nights(self):
        """The number of nights booked for the staycation

        :getter: Return the number of nights booked for the staycation
        :rtype: int

        """

        return self._nights

    @property
    def cost(self):
        """The cost of the staycation per night

        :getter: Return the cost per night for the staycation
        :setter: Set the existing cost with `new_cost` (float)
        :rtype: float

        """

        return self._cost

    @cost.setter
    def cost(self, new_cost):
        self._cost = float(new_cost)

    @property
    def voucher_allowed(self):
        """Whether voucher usage is allowed.

        :getter: Return whether voucher usage is allowed.
        :setter: Set the existing voucher permission to `allowed` (bool)
        :rtype: bool

        """

        return self._voucher_allowed

    @voucher_allowed.setter
    def voucher_allowed(self, allowed):
        self._voucher_allowed = allowed

    def cost_per_night(self):
        """Computes the cost per night for the staycation.

        Based on the number of nights in `self._nights`, we use compute the cost
        per night using `self._cost` / `self._nights` to obtain the base cost
        per night.

        Returns:
            cost_per_night (float): Cost divided by the number of nights booked.

        """

        cost_per_night = self._cost / self._nights
        return cost_per_night

    def is_cheaper(self, other):
        """Compares between two Staycation instances to determine which is cheaper.

        Given another Staycation instances, the calling instance of the method
        will be compared with the given Staycation instance (other) and
        determining if it is cheaper based on cost per night.

        Args:
            other (Staycation): Another Staycation class instance

        Return:
            (bool) : Return True if caller is cheaper, False if it more
                expensive per night.

        """

        return self.cost_per_night() < other.cost_per_night()

    def __str__(self):
        return (
            f"{self._hotel_name} "
            f"Nights: {self._nights} "
            f"Current Price: ${self._cost:.0f} or "
            f"${self.cost_per_night():.2f} per night "
            f"Voucher allowed: {'Yes' if self._voucher_allowed else 'No'}"
        )


# Q1(c)
class Booking:
    """A class to represent booking information for a staycation by a customer.

    """

    def __init__(self, customer, staycation, check_in_date):
        """Constructs and initialises all necessary attributes for the
        Booking object

        The `__init__` method initialises four attributes.

        Args:
            customer (Customer): A Customer class instance
            staycation (Staycation): A Staycation class instance
            check_in_date (datetime): The check in date indicated during the
                time of booking

        """

        self._customer = customer
        self._staycation = staycation
        self._check_in_date = check_in_date
        self._cost = staycation.cost  # cost of staycation at time of booking

    @property
    def customer(self):
        """The Customer instance who made the booking.

        :getter: Return the Customer instance
        :rtype: Customer

        """

        return self._customer

    @property
    def staycation(self):
        """The Staycation instance who booking was made for.

        :getter: Return the Staycation instance
        :rtype: Staycation

        """

        return self._staycation

    @property
    def cost(self):
        """The cost of the staycation at the point of booking.

        :getter: Return the cost of the staycation at the time of booking.
        :rtype: float

        """

        return self._cost

    @property
    def check_in_date(self):
        """The date of checking into the staycation.

        :getter: Return the check in date.
        :rtype: datetime

        """

        return self._check_in_date

    def check_out_date(self):
        """Compute the check out date based on the nights booekd for staycation.

        Given the check in date, the check out date is computed based on the
        number of nights booked where check out date = check in date +
        no. of nights booked.

        Returns:
            date (datetime): The computed check-out date

        """

        nights = self._staycation.nights
        date = self._check_in_date + timedelta(days=nights)
        return date

    def hotel_name(self):
        """Returns the staycation instance's hotel name"""
        return self._staycation.hotel_name

    def cost_difference_from_current(self):
        """Compute the cost difference between cost at booking and
        latest staycation's cost, if updated.

        Calling the Staycation instance's `cost` method and compare with the
        `self._cost` attribute initialised instantiated Booking instance.
        As `self._cost` remains unchanged after initialised, if changes are
        made to the cost of the Staycation instance, we return the difference.
        Else, if no changes were made, default is [0]

        Returns:
            cost_difference (float): Difference between Staycation latest cost
                and cost at booking

        """

        cost_difference = self._staycation.cost - self._cost
        return cost_difference

    def __str__(self):
        hotel_name = self._staycation.hotel_name
        nights = self._staycation.nights
        cost = self._cost  # using Booking's ._cost for initialised cost value
        cost_per_night = cost / nights  # initialised cost to prevent changes
        voucher_allowed = self._staycation.voucher_allowed
        check_in_date = self._check_in_date.strftime("%d %b %Y")
        check_out_date = self.check_out_date().strftime("%d %b %Y")
        customer_name = self._customer.name
        customer_contact = self._customer.contact

        return (
            f"{hotel_name} "
            f"Nights: {nights} "
            f"Current Price: ${cost:.0f} or ${cost_per_night:.2f} per night "
            f"Voucher allowed: {'Yes' if voucher_allowed else 'No'}\n"
            f"Booked at: ${cost:.0f} "
            f"Check-in Date: {check_in_date} "
            f"Check-out Date: {check_out_date}\n"
            f"{customer_name} {customer_contact}"
        )


def main():
    # Q1(d)(i)
    print("Creating Customer object...\n")
    c1 = Customer("Peter", "99998888")
    print(c1)
    # changing c1's number to 99998844
    print("Changing Peter's from 99998888 to 99998844.\n")
    previous_contact = c1.contact
    # Changing to new contact
    c1.contact = "99998844"
    print(c1)
    print(
        f"The customer: {c1.name} has changed contact from "
        f"{previous_contact} to {c1.contact}\n"
    )

    # Q1(d)(ii)
    # Creating two Staycation objects
    print("\nCreating two Staycation objects...\n")
    s1 = Staycation("Grand Marina", 2, 398, False)
    s2 = Staycation("Hotel Bugis", 1, 168)
    print(s1, s2, sep="\n")
    # Checking if first staycation is cheaper than second
    print(
        "Is the first staycation cheaper than the second?: "
        f"{'Yes' if s1.is_cheaper(s2) else 'No'}\n"
    )

    # Q1(d)(iii)
    # Creating Booking object
    print("\nCreating Booking object...\n")
    b1 = Booking(c1, s1, datetime(2021, 6, 30))
    print(b1)

    # Updating the cost of staycation from $398 to $438
    print(
        "\nComputing cost difference between time of "
        "booking vs. latest staycation cost...\n"
    )
    print("Changing staycation cost to $438.")
    s1.cost = 438.00
    print(
        f"The cost at the point of booking is ${b1.cost:.2f}. "
        "The computed cost difference with the latest cost of staycation is "
        f"${b1.cost_difference_from_current():.2f}."
    )


if __name__ == "__main__":
    main()
