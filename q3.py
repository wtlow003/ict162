# Q3(A)
from datetime import datetime
from q2 import Book, Media, Loan, ItemCopy


class LibraryException(Exception):
    """Exception class for exceptions raised in Library application.
    """


class LibraryPaymentException(LibraryException):
    """Exception class for exceptions raised in Library application involving
    payment amount.
    """

    def __init__(self, amount, message):
        super().__init__(message)
        self._amount = amount

    @property
    def amount(self):
        return self._amount


# Q3(B)
class Member:
    """A class to represent a member of the Library

    The member class details the member's id, name, fines owed and loans that
    were made by the member.

    Attributes:
        LOAN_QUOTA (int): The loan quota for a standard member, default to [4].

    Example:
        >>> member = Member('S101', 'Jensen')
    """
    _LOAN_QUOTA: int = 4

    def __init__(self, member_id: str, name: str) -> None:
        self._member_id = member_id
        self._name = name
        self._amount_owed = 0
        self._loans = []

    @classmethod
    def get_loan_quota(cls) -> int:
        """Return the loan quota set for the member class
        """
        return cls._LOAN_QUOTA

    @property
    def member_id(self) -> str:
        """

        :getter:
        :rtype:
        """
        return self._member_id

    @property
    def amount_owed(self) -> float:
        """

        :getter:
        :rtype:
        """
        return self._amount_owed

    def past_loans(self, title: str = None) -> list:
        """Return a list of loans with returned items.
        """
        past_loans = []
        # if title is supplied
        if title:
            for loan in self._loans:
                # check for matching title in loans and return date available
                if loan.loan_title() == title and loan.return_date is not None:
                    past_loans.append(loan)
        # no title is supplied
        else:
            # check for loan with return date
            past_loans = [loan for loan in self._loans if loan.return_date is not None]
        return past_loans

    def present_loans(self, title: str = None) -> list:
        """Return a list of loans with unreturned items.
        """
        present_loans = []
        # if title is supplied
        if title:
            for loan in self._loans:
                if loan.loan_title() == title and loan.return_date is None:
                    present_loans.append(loan)
        # no title is supplied
        else:
            # check for the loan with no return date
            present_loans = [loan for loan in self._loans if loan.return_date is None]
        return present_loans

    # TODO: double check on the logic
    def search_loan_for(self, title: str) -> Loan:
        """Return the first loan with unreturned item with a matching title.

        If no such loan exist, the method will return the last returned loan with
        a matching title, else returns `None`.

        Return:
            loan (Loan): Search for unreturned loan first, if not avaiable, then
                the last returned item will be returned, default to [None].
        """
        loan = None
        unreturned_loans = self.present_loans(title)
        returned_loans = self.past_loans(title)
        if unreturned_loans:
            loan = unreturned_loans[0]  # first matched loan
        elif not unreturned_loans and returned_loans:
            # sort the returned loan by date and return the last matched item
            returned_loans.sort(key=lambda loan: loan.return_date, reverse=True)
            loan = returned_loans[0]    # last returned matched item
        return loan

    def count_current_loan(self) -> int:
        """Count the number of unreturned items loaned.
        """
        return len(self.present_loans())

    def quota_reached(self) -> bool:
        """Indicate whether if the current number of loans is at the loan quota.
        """
        return self.count_current_loan() == type(self)._LOAN_QUOTA

    def borrow_item(self, item_copy: ItemCopy, date_borrowed: datetime) -> bool:
        """Method to allow a member to borrow a copy of an item, thereafter
        becoming a loan `Loan`.

        Upon borrowing the item, the item will be set to unavailable for others
        to borrow.

        The `borrow_item` method raises certain exception as follows:
            1. If `item_copy` provided is unavailable (already borrowed out).
            2. If member's `LOAN_QUOTA` has been reached.
            3. If the member has an outstanding fines.

        Return:
            (bool): Indicate whether the loan of the item copy was successful.
        """
        # `item_copy` is already borrowed out (unavailable)
        if not item_copy.available:
            raise LibraryException(f"Unavailable: {item_copy}")
        if self.quota_reached():
            raise LibraryException("Loan quota reached")
        # TODO: check logic for outstanding fines
        # TODO: check type of exception to raise
        if self._amount_owed > 0:
            raise LibraryException(f"You have ${self._amount_owed:.2f} outstanding fines. "
                                   "Do you want wish to pay your fines now? (y/n): ")

        loan = Loan(item_copy, date_borrowed)       # creating the loan
        self._loans.append(loan)        # adding to the member's loans
        item_copy.available = False     # setting item to unavailable
        return True

    def renew(self, title: str, renew_date: datetime) -> bool:
        """Method to allow member to renew the due date of the loaned item

        The `renew` method raises certain exceptions as follows:
            1. Provided title for renewal does not match all loans
            2. Provided title does not match existing loans but matched past loans.
            3. Provided title has a match, but renewal date exceed due date.

        Return:
            (bool): Indicate whether the loan is renewed
        """
        matched_loans = self.search_loan_for(title)
        past_loans = self.past_loans(title)
        present_loans = self.present_loans(title)

        if not matched_loans:
            raise LibraryException(f"There is no loan recorded for {title}")
        if not present_loans and past_loans:
            raise LibraryException(f"Item has been returned on {matched_loans.return_date}")
        if matched_loans and matched_loans.due_date < renew_date:
            raise LibraryException(
                f"Renewal date: {renew_date} exceed due date: {matched_loans.due_date}")
        return matched_loans.renew(renew_date)

    def return_item(self, title: str, return_date: datetime) -> bool:
        """Method to allow members to return the item that they loaned

        Uponing returning the item, the fines is also recorded if any fines are
        incurred. Item copy will also be set to available thereafter.

        The `return_item` method raises certain exceptions as follows:
            1. Provided title for returning does not match all loans
            2. Provided title does not match exisitng loans but matched past loans

        Return:
            (bool): Indicate whether the loan item has been returned
        """
        matched_loans = self.search_loan_for(title)
        past_loans = self.past_loans(title)
        present_loans = self.present_loans(title)

        if not matched_loans:
            raise LibraryException(f"There is no loan recorded for {title}")
        if not present_loans and past_loans:
            raise LibraryException(f"Item has been returned on {matched_loans.return_date}")

        matched_loans.return_date = return_date     # update with return date
        # retrieving fines, if any
        fines_incurred = matched_loans.get_fines()
        if fines_incurred:
            self._amount_owed += fines_incurred     # fines added to `amount_owed`
        return True

    def pay(self, amount: float) -> float:
        """
        """
        pass

    def loan_str(self, loans: list = None) -> str:
        """String representation of the loans the member has, given no specific
        list of loans.

        If a list of loan is given, it returns the string representation of such
        loans in the list instead.

        Return:
            loan_str (str): a string representation of given loans by a member,
            default to [`self._loans`]
        """
        loan_str = '\n'.join([str(loan) for loan in self._loans])   # all loans
        if loans is not None:
            loan_str = '\n'.join([str(loan) for loan in loans])  # selected loans
        return loan_str

    def __str__(self):
        # if no items are returned, `get_fines` method in Loan class will return
        # -1, hence, we need set the amount owed 0 and only return proper values
        # items are returned and check for fines for exceeding due date.
        amount_owed = self._amount_owed
        past_loans = self.past_loans()
        present_loans = self.present_loans()
        return (f"Id: {self._member_id} {self._name} Owed: ${amount_owed:.2f}"
                f"\nPast loans:"
                f"\n{'No past loans' if not past_loans else self.loan_str(past_loans)}"
                f"\nPresent loans:"
                f"\n{'No outstanding loans' if not present_loans else self.loan_str(present_loans)}"
                f"\nOutstanding loans: {len(present_loans)}\n")


class JuniorMember(Member):
    """A class that represents a junior member, which is below a standard
    member.

    The JuniorMember class does not defined its own constructor but inherit
    from the parent Member class.

    Attributes:
        LOAN_QUOTA (int): The loan quota for a junior member, default to [2].

    Examples:
        >>> junior_member = JuniorMember('S100', 'Jensen')
    """

    _LOAN_QUOTA: int = 2

    def __init__(self, member_id: str, name: str):
        super().__init__(member_id, name)


def main():
    """Test cases to align with TMA output
    """
    b1 = Book('The Road to Forget', 2009, 39.90, ['Thomas Rosicky'])
    b2 = Book('Asia Food and Culture', 2018, 19.90, ['Maddison James'])
    m1 = Book('Dark Knight', 2017, 6.99, ['Christopher Nolan'])
    m2 = Media('Powerpoint Presentation Tips', 2000, 20.00)
    print(b1, b2, m1, m2, sep='\n')
    ic1 = ItemCopy(b1)
    ic2 = ItemCopy(b2)
    ic3 = ItemCopy(m1)
    ic4 = ItemCopy(m2)
    print(ic1, ic2, ic3, ic4, sep='\n')
    print('\n')

    # Member borrowing the loan items
    mem1 = Member('S123', 'John')
    print(mem1)
    print('\n')
    mem1.borrow_item(ic1, datetime(2021, 3, 1))
    mem1.borrow_item(ic2, datetime(2021, 3, 1))
    mem1.borrow_item(ic3, datetime(2021, 3, 1))
    mem1.borrow_item(ic4, datetime(2021, 3, 1))
    # returning items
    print(mem1.return_item('Dark Knight', datetime(2021, 3, 17)))
    print(mem1)

    # # Junior member borrowing the loan items
    # jmem1 = JuniorMember('S123', 'John')
    # print(jmem1)
    # print('\n')
    # jmem1.borrow_item(ic1, datetime(2021, 3, 1))
    # jmem1.borrow_item(ic2, datetime(2021, 3, 1))
    # jmem1.borrow_item(ic3, datetime(2021, 3, 1))
    # jmem1.borrow_item(ic4, datetime(2021, 3, 1))
    # # returning items
    # jmem1.return_item('Dark Knight', datetime(2021, 3, 17))
    # print(jmem1)


if __name__ == '__main__':
    main()
