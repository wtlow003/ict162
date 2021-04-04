"""
Created on 31 Mar 2021

@author: Low Wei Teck

04 Apr 2021: Added latest docstring, pending testing on logics and
             confirmation on minor TMA questions

"""


from abc import ABC, abstractmethod
from datetime import datetime, timedelta


class Item(ABC):
    """An abstract superclass to represent one item in a library.

    Attributes:
        loan_duration (int): Loan duration for an item in the library,
            default to [14].

    """
    _LOAN_DURATION: int = 14

    def __init__(self, title: str, year_published: int, cost: float):
        """Constructs and initialises all necessary attributes for the Item
        superclass.

        The `__init__` method initialises three attributes.

        Args:
            title (str): Title of the item
            year_published (int): Published year of the item
            cost (float): Actual cost of the item
        """
        self._title = title
        self._year_published = year_published
        self._cost = cost

    @property
    def title(self) -> str:
        """The title of the item.

        :getter: Return the title of the item
        :rtype: str
        """
        return self._title

    @property
    def year_published(self) -> int:
        """The year of the publishing of the item.

        :getter: Return the item's year of publishing
        :rtype: int
        """
        return self._year_published

    @property
    def cost(self) -> float:
        """The cost of the item.

        :getter: Return the cost of the item
        :rtype: float
        """
        return self._cost

    @classmethod
    def get_loan_duration(cls) -> int:
        """Return the class default loan duration for items in a library
        """
        return cls._LOAN_DURATION

    @classmethod
    def set_loan_duration(cls, new_duration: int):
        """Set the new default loan duration for items in a library
        """
        cls._LOAN_DURATION = new_duration

    @abstractmethod
    def get_admin_charge(self) -> float:
        """Return the default adminstrative charges, or compute if any.
        """
        pass

    @abstractmethod
    def get_fines_per_day(self) -> float:
        """
        Return the fines incurred per day if exceeded the due date.
        """
        pass

    def lost_charges(self) -> float:
        """
        Compute the lost charges
        based on `get_admin_charge()` + cost of item, `self._cost`
        """
        return self.get_admin_charge() + self._cost

    def __str__(self) -> str:
        return f"{self._title} {self._year_published} Cost: ${self._cost:.2f}"


class Book(Item):
    """A class to represent a book in the library.

    The Book class inherit the instance variables from the parent Item class,
    and also introduce `_authors` as an additional instance variable.

    Example:
        >>> book = Book('ICT162', 2019, 19.90, ['SUSS'])
    """

    def __init__(self, title: str, year_published: int, cost: float, authors: list):
        """Constructs and initialises all necessary attributes for the
        inherited subclass object of Item class.

        The `__init__` method initialises three (superclass) + 1 (subclass)
        instance attributes.

        Args:
            title (str): Title of the item
            year_published (int): Published year of the item
            cost (float): Actual cost of the item
            authors (list): A list of strings containing the author's names
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
            admin_charge (float): The percentage in decimal based on `year_published`.
        """
        year_diff_from_curr = datetime.now().year - self._year_published
        # If books older than 9 years from year pub using today's date
        if year_diff_from_curr > 9:
            admin_charge = 0.10
        else:
            admin_charge = ((10 - year_diff_from_curr) / 10)
        return admin_charge

    def get_fines_per_day(self) -> float:
        """Return the fines per day for exceeding the due date
        """
        return 0.25

    def __str__(self) -> str:
        authors = ', '.join(self._authors)
        return f"{super().__str__()} By {authors}"


class Media(Item):
    """A class to represent a media in the library.

    The Media class does not defined its own constructor but inherit from the
    parent Item class.

    Attributes:
        loan_duration (int): The loan duration set for media item,
            default to [3].

    Example:
        >>> media = Media('ICT162', 2019, 19.90)
    """
    _LOAN_DURATION = 3

    def get_admin_charge(self) -> float:
        """
        For media item, adminstrative charge is set at 1.5x of the cost price.
        """
        return 1.5 * self._cost

    def get_fines_per_day(self) -> float:
        """Return the fines per day for exceeding the due date
        """
        return 2.50


class ItemCopy:
    """A class to represent a copy of the item in the library.

    The `ItemCopy` can be defined as a copy of a book or media that a member
    can borrow from the library.

    Attributes:
        NEXT_ID (int): The id assigned to each copy of the item available,
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
        """Constructs and initialises all necessary attributes for the
        `ItemCopy` class.

        The `__init__` method initialises four attributes.

        Args:
            title (str): Title of the item
            year_published (int): Published year of the item
            cost (float): Actual cost of the item
            authors (list): A list of strings containing the author's names
        """
        self._item = item
        self._copy_id = self._NEXT_ID
        self._available = True
        # increase next_id by 1, everytime we instantiate a ItemCopy instance
        type(self)._NEXT_ID += 1

    @property
    def item(self) -> Item:
        """The item that we are making a copy of

        :getter: Return the item we are making a copy of
        :rtype: Item
        """
        return self._item

    @property
    def copy_id(self) -> int:
        """The copy id of the item copy that we are have instantiated

        :getter: Return the copy id of the item copy
        :rtype: int
        """
        return self._copy_id

    @property
    def available(self) -> bool:
        """The status of the item copy, where either available (True) or
        unavailable (False)

        :getter: Return the availability status of the item copy
        :setter: Set the availabity status of the item copy
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, status: bool) -> None:
        self._available = status

    def __str__(self) -> str:
        return (f"CopyId: {self._copy_id} "
                f"{self._item} "
                f"Available: {self._available}")


class Loan:
    """A class to represent a loan made for a copy of an item

    Example:
        >>> book = Book('ICT162', 2019, 19.90, ['SUSS'])
        >>> item_copy = ItemCopy(book)
        >>> loan = Loan(item_copy)
    """

    def __init__(self, item_copy: ItemCopy, loan_date: datetime):
        """Constructs and initialises all necessary attributes for the Loan class


        The `__init__` method initialises three instance attributes.

        Args:
            item_copy (ItemCopy): The copy of the item that a loan is made for
            due_date (datetime): The date of which the loan must be returned
                prior to any form of renewal, before fines are incurred.
            return_date (datetime): The date of which the loan is return back to
                the library.
        """
        self._item_copy = item_copy
        self._due_date = (loan_date +
                          timedelta(days=item_copy.item.get_loan_duration()))
        self._return_date = None

    @property
    def due_date(self) -> datetime:
        """The date of which the loan must be returned before fines are incurred.
        The due date can be extended using `renew` method if renewal is done
        before the due date.

        :getter: Return the current due date for the loan of the copy of the item
        :rtype: datetime
        """
        return self._due_date

    @property
    def return_date(self) -> datetime:
        """The date of which the loan is returned back to the library, default to
        [None]

        :getter: Return the date of which the loan is returned
        :setter: Set the date of which the loan is returned back to the library
        :rtype: datetime
        """
        return self._return_date

    @return_date.setter
    def return_date(self, return_date) -> None:
        self._return_date = return_date

    def loan_title(self) -> str:
        """The title of the loaned copy of the item.
        """
        return self._item_copy.item.title

    def copy_id(self) -> int:
        """The copy id of the loaned copy of the item.
        """
        return self._item_copy.copy_id

    # TODO: review on the need for renew_date
    def renew(self, renew_date: datetime) -> bool:
        """Method to extend the due date of the loan provided that the renewal
        date is before the current due date. If the date of attempted renewal is
        after the due date, the renewal cannot be proceeded.

        The new due date is computed as:
            `due_date` = curr_due_date + `Item.get_loan_duration()`

        Return:
            (bool): True if renewal is successful, else False.
        """
        # renew_date = datetime.now()
        if renew_date < self._due_date:
            self._due_date += timedelta(days=self._item_copy.item.get_loan_duration())
            return True
        return False

    def get_fines(self) -> float:
        """Method to compute the fines of the loan given the number of days, of
        which the loan has exceeded the due date.

        The fines are only computed when the loan is returned. The computation:
            fines = days_exceed * `Item.get_fines_per_day()`

        If the loan has not been returned, the fines will be returned as -1.

        Return:
            fines (float): -1 if the loan has not been returned, else the fines
                will be compute based on days exceeded and fines per day for the
                type of item.
        """
        fines = -1
        if self._return_date is not None:
            days_exceed = (self._return_date - self._due_date
                           if self._return_date > self._due_date else 0)
            fines = days_exceed.days * self._item_copy.item.get_fines_per_day()
        return fines

    def lost_charges(self) -> float:
        """The lost charges associated with the copy of the item loaned if the
        loan was reported to be lost.
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


if __name__ == '__main__':
    # b1 = Book('The Road to Forget', 2020, 35.00, ['Justin Grave', 'Tom Aplesson'])
    # print(b1.year_published)
    # print(b1.get_admin_charge())
    # print(b1.get_loan_duration())
    # print(b1)
    # print(help(b1))
    # m1 = Media('Asia Food and Culture', 2019, 30.00)
    # print(m1.get_admin_charge())
    # print(m1.get_fines_per_day())
    # print(m1.get_loan_duration())
    # ic1 = ItemCopy(b1)
    # print(ic1)
    # ic2 = ItemCopy(m1)
    # ic2.available = False
    # print(ic2)
    # ic3 = ItemCopy(b1)
    # ic3.available = False
    # print(ic3)
    # print(help(Loan))
    # l1 = Loan(ic3, datetime(2021, 3, 15))
    # print(l1)
    # print(l1.renew())
    # print(l1)
    # l1.return_date = datetime(2021, 4, 12)
    # print(l1)
    # print(l1.get_fines())
    # print(l1.lost_charges())
    # print(l1.loan_title())
    print(help(Item))
    print(help(Book))
    print(help(Media))
    print(help(ItemCopy))
    print(help(Loan))
