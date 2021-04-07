"""
Created on 31 Mar 2021

@author: Low Wei Teck

04 Apr 2021: Added latest docstring, pending testing on logics and
             confirmation on minor TMA questions

"""


from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# Q2(A)
class Item(ABC):
    """An abstract superclass to represent one item in a library.

    Attributes:
        LOAN_DURATION (int): Loan duration for an item in the library,
            default to [14].

    """
    _LOAN_DURATION: int = 14

    def __init__(self, title: str, year_published: int, cost: float):
        """The `__init__` method initialises three attributes.

        Args:
            title: Title of the item
            year_published: Published year of the item
            cost: Actual cost of the item

        """
        self._title = title
        self._year_published = year_published
        self._cost = float(cost)

    @property
    def title(self) -> str:
        """Title of the item.

        :getter: Return the title of the item
        :rtype: str

        """
        return self._title

    @property
    def year_published(self) -> int:
        """Year of the item published.

        :getter: Return the item's year of published
        :rtype: int

        """
        return self._year_published

    @property
    def cost(self) -> float:
        """Cost of the item.

        :getter: Return the cost of the item
        :rtype: float

        """
        return self._cost

    @classmethod
    def get_loan_duration(cls) -> int:
        """Return the class's default `LOAN_DURATION` for items in a library
        """
        return cls._LOAN_DURATION

    @classmethod
    def set_loan_duration(cls, new_duration: int):
        """Set the new default `LOAN_DURATION` for items in a library
        """
        cls._LOAN_DURATION = new_duration

    @abstractmethod
    def get_admin_charge(self) -> float:
        """Return the default adminstrative charges, or compute if any."""
        pass

    @abstractmethod
    def get_fines_per_day(self) -> float:
        """Return the fines incurred per day if exceeded the due date."""
        pass

    def lost_charges(self) -> float:
        """Return the computed the lost charges

        The lost charge can be computed as:
            `lost_charges` = `get_admin_charge()` + `cost`

        """
        return self.get_admin_charge() + self._cost

    def __str__(self) -> str:
        return f"{self._title} {self._year_published} Cost: ${self._cost:.2f}"


# Q2(B)(i)
class Book(Item):
    """A class to represent a book in the library.

    The Book class inherit instance variables from the parent Item class,
    with `authors` as an additional instance variable.

    Examples:
        >>> book = Book('ICT162', 2019, 19.90, ['SUSS'])
    """

    def __init__(self, title: str, year_published: int, cost: float, authors: list):
        """The `__init__` method initialises four instance attributes.

        Args:
            title: Title of the item
            year_published: Published year of the item
            cost: Actual cost of the item
            authors: A list of strings containing the author's names
        """
        super().__init__(title, year_published, cost)
        self._authors = authors

    # TODO: Check the calculation using the formula
    def get_admin_charge(self) -> float:
        """Compute the adminstrative charges based on the year of published.

        The adminstrative charges is determined based on the year of publishing,
        where if the book is older than 9 years from today's date (year), it is
        set at a constant rate of 10%. Meanwhile if the book is relatively new,
        the adminstrative charges is computed based on:

            `admin_charge` = (10 - (`this_year` - `year_published`)) / 10

        Return:
            admin_charge: The percentage in decimal based on `year_published`.
        """
        year_diff_from_curr = datetime.now().year - self._year_published
        # Books older than 9 years since year published has a fixed rate of 10%
        if year_diff_from_curr > 9:
            admin_charge = 0.10
        else:
            admin_charge = ((10 - year_diff_from_curr) / 10)
        return admin_charge

    def get_fines_per_day(self) -> float:
        """Return the fines per day for exceeding the due date"""
        return 0.25

    def __str__(self) -> str:
        authors = ', '.join(self._authors)
        return f"{super().__str__()} By {authors}"


# Q2(B)(i)
class Media(Item):
    """A class to represent a media in the library.

    The Media class does not defined its own constructor but inherit from the
    parent Item class.

    Attributes:
        loan_duration: The loan duration set for media item,
            default to [3].

    Examples:
        >>> media = Media('ICT162', 2019, 19.90)

    """
    _LOAN_DURATION: int = 3

    def get_admin_charge(self) -> float:
        """Compute adminstrative charge, which is set at 1.5x of the cost price
        for Media class.
        """
        return 1.5 * self._cost

    def get_fines_per_day(self) -> float:
        """Return the fines per day for exceeding the due date"""
        return 2.50


# Q2(C)
class ItemCopy:
    """A class to represent a copy of the item in the library.

    The `ItemCopy` class can be defined as a copy of a book or media that a
    member can borrow from the library.

    Attributes:
        NEXT_ID: The id assigned to each copy of the item available,
            starting from 1 and auto-increasing with each new `ItemCopy`
            instantiated.

    Example:
        >>> book = Book('ICT162', 2019, 19.90, ['SUSS'])
        >>> media = Media('ICT162', 2019, 19.90)
        >>> item_copy = ItemCopy(book)
        >>> item_copy = ItemCopy(media)

    """
    _NEXT_ID: int = 1

    def __init__(self, item: Item):
        """The `__init__` method initialises four attributes.

        Args:
            item: Item that exist in the library's collection

        """
        self._item = item
        # :int: Each item copy has a unique copy id upon instantiating
        self._copy_id = self._NEXT_ID
        # :bool: True when no one borrowed, False if otherwise.
        self._available = True
        # Increase next_id by 1, everytime we instantiate a ItemCopy instance
        type(self)._NEXT_ID += 1

    @property
    def item(self) -> Item:
        """Item that we are making a copies of

        :getter: Return the item we are making a copy of

        """
        return self._item

    @property
    def copy_id(self) -> int:
        """Copy id of the item copy that we are have instantiated

        :getter: Return the copy id of the item copy

        """
        return self._copy_id

    @property
    def available(self) -> bool:
        """Status of the item copy, True when available, False if otherwise.

        :getter: Return the availability status of the item copy
        :setter: Set the availabity status of the item copy, True if available
            (not borrowed), False if otherwise

        """
        return self._available

    @available.setter
    def available(self, status: bool) -> None:
        self._available = status

    def __str__(self) -> str:
        return (f"CopyId: {self._copy_id} "
                f"{self._item} "
                f"Available: {self._available}")


# Q2(D)
class Loan:
    """A class to represent a loan made for a copy of an item

    Examples:
        >>> book = Book('ICT162', 2019, 19.90, ['SUSS'])
        >>> item_copy = ItemCopy(book)
        >>> loan = Loan(item_copy)

    """

    def __init__(self, item_copy: ItemCopy, loan_date: datetime):
        """The `__init__` method initialises three instance attributes.

        Args:
            item_copy: The copy of the item that a loan is made for
            loan_date: Date of the loan occured, used to compute the `due_date`,
                where `due_date` = `loan_date` + `Item.get_loan_duration()`

        """
        self._item_copy = item_copy
        # `due_date` = `loan_date` +  `Item.get_loan_duration()`
        self._due_date = (loan_date +
                          timedelta(days=item_copy.item.get_loan_duration()))
        # :datetime:  Return date of the loan, default to [None].
        self._return_date = None

    # TODO: temp solution for item_copy to retrieve available in return item
    # TODO: check why is it here
    @property
    def item_copy(self) -> ItemCopy:
        """Item copy borrowed in the loan process

        :getter: Returns the item copy borrowed in the loan

        """
        return self._item_copy

    @property
    def due_date(self) -> datetime:
        """The date of which the loan must be returned before fines are incurred.
        The due date can be extended using `renew` method if renewal is done
        on or before the due date.

        :getter: Returns the due date of the loan for the copy of the item

        """
        return self._due_date

    @property
    def return_date(self) -> datetime:
        """Return date of the loan, until the item has indicated to be returned,
        default to [None]

        :getter: Returns the returned date of the loan
        :setter: Set the returned date of the loan

        """
        return self._return_date

    @return_date.setter
    def return_date(self, return_date) -> None:
        self._return_date = return_date

    def loan_title(self) -> str:
        """Returns the title of the loaned copy of the item."""
        return self._item_copy.item.title

    def copy_id(self) -> int:
        """Returns the copy id of the loaned copy of the item."""
        return self._item_copy.copy_id

    # TOOD: Jenny confirmed the need to add `renew_date` as a new arg.
    def renew(self, renew_date: datetime) -> bool:
        """Extend the due date of the loan provided that the renewal date,
        is on or before the current due date.

        If the date of attempted renewal is after the due date, the renewal
        cannot be proceeded.

        The new due date is computed as:
            `due_date` += `Item.get_loan_duration()`

        Args:
            renew_date: The date of which the renewal was requested.

        Returns
            True if renewal is successful, False if otherwise.

        """
        # renew_date = datetime.now()
        if renew_date <= self._due_date:    # before up to the actual due date
            self._due_date += timedelta(days=self._item_copy.item.get_loan_duration())
            return True

        return False

    def get_fines(self) -> float:
        """Compute the loan fines given the number of days the loan had exceeded
        the due date. The fines are only computed when the loan is returned.

        The computation:
            fines = days_exceed * `Item.get_fines_per_day()`

        If the loan has not been returned, the fines will be returned as -1.

        Returns:
            fines: -1 if the loan has not been returned, else the fines
                will be compute based on days exceeded and fines per day for the
                type of item.

        """
        fines = -1

        # Loans has been returned
        if self._return_date is not None:
            days_exceed = (self._return_date - self._due_date
                           if self._return_date > self._due_date else 0)
            # Loan not returned on time (`due_date` == `return_date`)
            if days_exceed:
                fines = (
                    days_exceed.days * self._item_copy.item.get_fines_per_day())
            else:
                fines = 0

        return float(fines)

    def lost_charges(self) -> float:
        """Returns lost charges associated with the copy of the item loaned if
        the loan was reported to be lost.

        """

        return self._item_copy.item.lost_charges()

    def __str__(self) -> str:
        copy_id = self._item_copy.copy_id
        title = self._item_copy.item.title
        due_date = self._due_date.strftime('%d %b %Y')
        return_date = self._return_date.strftime(
            '%d %b %Y') if self._return_date is not None else 'On Loan'

        return (f"Loan Copy id: {copy_id} {title}"
                f"\n\t Due date: {due_date} "
                f"Return on: {return_date}")


def main():
    """Sequences of events to test the classes defined"""

    b1 = Book('The Road to Forget', 2020, 35.00, ['Justin Grave', 'Tom Aplesson'])
    print(b1.year_published)
    print(b1.get_admin_charge())
    print(b1.get_loan_duration())
    print(b1)
    print(help(b1))
    m1 = Media('Asia Food and Culture', 2019, 30.00)
    print(m1.get_admin_charge())
    print(m1.get_fines_per_day())
    print(m1.get_loan_duration())
    ic1 = ItemCopy(b1)
    print(ic1)
    ic2 = ItemCopy(m1)
    ic2.available = False
    print(ic2)
    ic3 = ItemCopy(b1)
    ic3.available = False
    print(ic3)
    print(help(Loan))
    l1 = Loan(ic3, datetime(2021, 3, 15))
    print(l1)
    print(l1.renew())
    print(l1)
    l1.return_date = datetime(2021, 4, 12)
    print(l1)
    print(l1.get_fines())
    print(l1.lost_charges())
    print(l1.loan_title())


if __name__ == '__main__':
    main()
