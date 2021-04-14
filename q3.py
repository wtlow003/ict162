"""
Created on 01 Apr 2021

@author: Low Wei Teck

06 Apr 2021: Completed working copy for q3.py, need further testing for get_admin_charge
             case.

"""


from datetime import datetime
from q2 import Book, Media, Loan, ItemCopy, Item


# Q3(A)
class LibraryException(Exception):
    """Exception class for exceptions raised in Library application."""


class LibraryPaymentException(LibraryException):
    """Exception class for exceptions raised in Library application involving
    payment amount.
    """

    def __init__(self, amount: float, message: str):
        super().__init__(message)
        self._amount = amount

    @property
    def amount(self):
        """Amount involved in raising `LibraryPaymentException`

        :getter: Return the amount involved in raising the exception
        :rtype: float

        """
        return self._amount


# Q3(B)(i)
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
        """Return the loan quota set for the member class"""
        return cls._LOAN_QUOTA

    @property
    def member_id(self) -> str:
        """The member id of the `Member`

        :getter: Return the member_id of the Member class object
        :rtype: str

        """
        return self._member_id

    @property
    def amount_owed(self) -> float:
        """The amount owed by the member from outstanding fines

        :getter: Return the amount currently owed by the member
        :rtype: float

        """
        return self._amount_owed

    def past_loans(self, title: str = None) -> list:
        """Return a list of loans with returned items.

        Args:
            title: The title of the item loaned previously, default to [None].

        Returns:
            past_loans: A list of past loans with matching titles.

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

        Args:
            title: The title of the item loaned currently, default to [None].

        Returns:
            present_loans: A list of present loans with matching titles.

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

        Args:
            title: The title of the item to be searched in the member's loan
                history.

        Returns:
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
        """Count the number of unreturned items loaned."""
        return len(self.present_loans())

    def quota_reached(self) -> bool:
        """Return True if current loan number reached quota, False otherwise."""
        return self.count_current_loan() == type(self)._LOAN_QUOTA

    def borrow_item(self, item_copy: ItemCopy, date_borrowed: datetime) -> bool:
        """Method to allow a member to borrow a copy of an item, thereafter
        becoming a loan `Loan`.

        Upon borrowing the item, the item will be set to unavailable for others
        to borrow.

        Args:
            item_copy: A copy of the item in the library to be borrowed.
            date_borrowed: The date of which the item copy is borrowed.

        Returns:
            (bool): Indicate whether the loan of the item copy was successful.

        Raises:
            LibraryException: Item copy is unavailable or loan quota is reached.
            LibraryPaymentException: If member has an existing fine unpaid.

        """
        # `item_copy` is already borrowed out (unavailable)
        if not item_copy.available:
            raise LibraryException(f"Unavailable: {item_copy}")
        if self.quota_reached():
            raise LibraryException("Loan quota reached")
        # TODO: check logic for outstanding fines
        # TODO: check type of exception to raise
        if self._amount_owed > 0:
            raise LibraryPaymentException(self._amount_owed,
                                          f"You have ${self._amount_owed:.2f} "
                                          "outstanding fines. "
                                          "Do you want wish to pay your fines now? (y/n): ")

        loan = Loan(item_copy, date_borrowed)       # creating the loan
        self._loans.append(loan)        # adding to the member's loans
        item_copy.available = False     # setting item to unavailable

        return True

    def renew(self, title: str, renew_date: datetime) -> bool:
        """Method to allow member to renew the due date of the loaned item

        Args:
            title: The title of the item copy loaned, that is to be renewed.
            renew_date: The date of which renewal is requested.

        Returns:
            (bool): Indicate whether the loan is renewed

        Raises:
            LibraryException: If no loan is detected, loan has already been
                returned or renewal date is beyond the original due date.

        """

        matched_loans = self.search_loan_for(title)
        past_loans = self.past_loans(title)
        present_loans = self.present_loans(title)

        if not matched_loans:
            raise LibraryException(f"There is no loan recorded for {title}")
        if not present_loans and past_loans:
            raise LibraryException(f"Item has been returned on {matched_loans.return_date}")
        if matched_loans and (matched_loans.due_date < renew_date):
            renew_date = renew_date.strftime('%d %b %Y')
            due_date = matched_loans.due_date.strftime('%d %b %Y')
            raise LibraryException(
                f"Date of renewal on {renew_date} exceed the existing due date on {due_date}")
        matched_loans.renew(renew_date)

        return True

    def return_item(self, title: str, return_date: datetime) -> bool:
        """Method to allow members to return the item that they loaned

        Upon returning the item, the fines is also recorded if any fines are
        incurred. Item copy will also be set to available thereafter.

        Args:
            title: The title of the item copy to be returned to the library.
            return_date: The date of each the loan is returned.

        Return:
            (bool): Indicate whether the loan item has been returned

        Raises:
            LibraryException: If title provided does not match any loans, or
                title matches items that have already been returned.

        """
        matched_loans = self.search_loan_for(title)
        past_loans = self.past_loans(title)
        present_loans = self.present_loans(title)

        if not matched_loans:
            raise LibraryException(f"There is no loan recorded for {title}")
        # TODO: fix the return date formatting.
        if not present_loans and past_loans:
            raise LibraryException(f"Item has been returned on {matched_loans.return_date}")

        matched_loans.return_date = return_date     # Update with return date
        fines_incurred = matched_loans.get_fines()
        if fines_incurred:
            self._amount_owed += fines_incurred     # Fines added to `amount_owed`

        return True

    def pay(self, amount: float) -> float:
        """Method to allow members to pay their outstanding fines

        Args:
            amount: The amount the member is paying for their outstanding fines.

        Returns:
            change (float): change if the amount paid exceed amount owed, default
            to [0].

        Raises:
            LibraryPaymentException: If the amount chosen by the member for the
                payment is less than 0.

        """
        if amount <= 0:
            raise LibraryPaymentException(amount,
                                          f"You owed ${self._amount_owed:.2f}. "
                                          f"Please pay an amount more than ${amount:.0f}.")
        # Change does not exists if you pay less than required
        change = amount - self._amount_owed if amount > self._amount_owed else 0
        # Maximum payable fines is exisitng outstanding fines
        # Only payable until the `_amount_owed` == 0
        self._amount_owed -= (amount - change)

        return change

    def loan_str(self, loans: list = None) -> str:
        """String representation of the loans the member has, given no specific
        list of loans.

        If a list of loan is given, it returns the string representation of such
        loans in the list instead.

        Args:
            loans: A list of loans given to be displayed, default to [None].

        Returns:
            loan_str (str): a string representation of given loans by a member,
            default to [`self._loans`]

        """
        loan_str = '\n'.join([str(loan) for loan in self._loans])   # all loans
        if loans is not None:
            loan_str = '\n'.join([str(loan) for loan in loans])  # selected loans

        return loan_str

    def __str__(self):
        amount_owed = self._amount_owed
        past_loans = self.past_loans()
        present_loans = self.present_loans()

        return (f"\nId: {self._member_id} {self._name} Owed: ${amount_owed:.2f}"
                f"\nPast loans:"
                f"\n{'No past loans' if not past_loans else self.loan_str(past_loans)}"
                f"\nPresent loans:"
                f"\n{'No outstanding loans' if not present_loans else self.loan_str(present_loans)}"
                f"\nOutstanding loans: {self.count_current_loan()}")


# Q3(B)(ii)
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


# Q3(C)
class Library:
    """A class to represent a library.

    The Library class consists of the information detailing the items, copies of
    items and members registered under the Library.

    Example:
        >>> library = Library()
    """

    def __init__(self):
        """
        """
        self._members = {}
        self._items = {}
        self._copy_items = []

    def add_item(self, item: Item) -> bool:
        """Add item to `_items` if item's title does not exist"""
        if item.title not in self._items.keys():
            self._items[item.title] = item
            return True
        return False

    def add_copy_item(self, item: Item) -> None:
        """Creates a copy item and adds to `_copy_items`"""
        copy_item = ItemCopy(item)
        self._copy_items.append(copy_item)

    def register_member(self, member: Member) -> bool:
        """Add a member to `_members` if member id does not exist"""
        if member.member_id not in self._members:
            self._members[member.member_id] = member
            return True
        return False

    def remove_member(self, member_id: str) -> Member:
        """Remove a member from `_members` based on the `member_id`"""
        return self._members.pop(member_id, None)   # Return None if no member

    def search_member(self, member_id: str) -> Member:
        """Search a member based on `member_id` from `_members``"""
        if member_id in self._members:
            return self._members[member_id]
        return None

    def search_copy_item(self, copy_id: int) -> ItemCopy:
        """Search a copy item based on `copy_id` from `_copy_items`"""
        matched = [copy for copy in self._copy_items if copy.copy_id == copy_id]
        # empty list -> False, list with element -> True
        if matched:
            return matched[0]
        return False

    # TODO: check logic and refactoring
    def get_available_copy_items(self) -> list:
        """Retrieving all item copies that are currently available

        Returns:
            available_item_copies: A list of item copies that is available.

        """
        available_item_copies = [copy for copy in self._copy_items
                                 if copy.available is True]
        return available_item_copies

    def copy_item_str(self, copy_item_list: list = None) -> str:
        """String representation of item copies in the Library class object"""
        if copy_item_list:
            copy_items = '\n'.join([str(copy) for copy in copy_item_list])
        else:
            copy_items = '\n'.join([str(copy) for copy in self._copy_items])
        return f"{copy_items}"

    def member_str(self) -> str:
        """String representation of members in the Library class object"""
        members = '\n'.join([str(mem) for mem in self._members.values()])
        return f"{members}"

    def item_str(self) -> str:
        """String representation of items in the Library class object"""
        items = '\n'.join([str(item) for item in self._items.values()])
        return f"{items}\n"

    def __str__(self) -> str:
        return (f"{self.item_str()}"
                f"\n{self.copy_item_str()}"
                f"\n{self.member_str()}")


# Q3(E)
# TODO: Check whether are applying try block too early.
class LibraryApplication:
    """
    """

    def __init__(self, library: Library):
        """
        """
        self._library = library

    @staticmethod
    def date_check(date_type: str) -> datetime:
        """Obtain date input and run a format validity check

        Args:
            date_type: Indicate what kind of date we are checking for
                >>> 'renew': checking for renewal date

        Returns:
            requested_date: Return the user inputted date that pass
                the format check
        """
        while True:
            requested_date = input(f"Enter {date_type} date in dd/mm/yyyy: ")
            date_format = "%d/%m/%Y"
            try:
                requested_date = datetime.strptime(requested_date, date_format)
                break
            except ValueError:
                print(f"{requested_date} is not in the format dd/mm/yyyy")

        return requested_date

    def member_check(self):
        """Obtain member id and run a validity check with `library`

        Returns:
            member: The member id if member is valid, else return empty string.

        """
        member_id = input("Enter member id: ")
        member = self._library.search_member(member_id.upper())
        if member is None:
            print("Invalid member id")

        return member

    # TODO: PLEASE FIX
    def option_1(self):
        """Allow users to borrow items through available copy ids
        """
        member = self.member_check()

        if member:
            print(
                f"Current number of loans: {member.count_current_loan()} "
                f"Quota: {member.get_loan_quota()}")

            if member.quota_reached():
                print("Quota reached. No more loan allowed")
            else:
                borrow_date = self.date_check('borrow')

                # while member.count_current_loan() < member.get_loan_quota():
                while not member.quota_reached():
                    try:
                        # Display all the available items in the library
                        available_items = self._library.get_available_copy_items()
                        available_items_ids = [avail.copy_id for avail in available_items]
                        print("Available items")
                        print(self._library.copy_item_str(available_items))

                        # Get user option for items to borrow, else exit current menu option
                        copy_item_choice = input("Enter the copy id or 0 to end: ")

                        if int(copy_item_choice) in available_items_ids:
                            item_copy = self._library.search_copy_item(int(copy_item_choice))
                            member.borrow_item(item_copy, borrow_date)
                            print(f"Sucessfully borrowed {item_copy.item.title}")
                        elif copy_item_choice == '0':
                            break
                        else:
                            print("Invalid copy id - does not match available items")
                    except LibraryPaymentException as pe:
                        # TODO: work on if people press other than y/n
                        payment_choice = input(pe)
                        if payment_choice.lower() == 'y':
                            # make the deduct from amount owed, assume full amount paid
                            member.pay(member.amount_owed)
                            member.borrow_item(item_copy, borrow_date)
                            print(f"Sucessfully borrowed {item_copy.item.title}")
                        elif payment_choice.lower() == 'n':
                            print("Please pay your fines first before borrowing")
                            break
                    except ValueError:
                        print(f"{copy_item_choice} is not a valid item copy choice")
                # # TODO: think of how to use `Member` quota exception
                if member.quota_reached():
                    print("Loan quota reached")

            print(member)

    def option_2(self):
        """Allow users to renew items through title"""
        member = self.member_check()

        if member:
            try:
                title = input("Enter title: ")
                renew_date = self.date_check('renew')
                # title check
                loan = member.search_loan_for(title)
                if loan and not loan.return_date:
                    # use Member's `renew` method to raise exceptions
                    member.renew(title, renew_date)  # renew the item
                    print(f"Successfully renewed {title}")
                elif loan and loan.return_date:
                    print("Item has been returned on "
                          f"{loan.return_date.strftime('%d %b %Y')}")
                else:
                    print(f"There is no loan recorded for {title}")
            except LibraryException as e:
                print(e)

            # Display member's info for verification
            print(member)

    def option_3(self):
        member = self.member_check()

        if member:
            return_date = self.date_check('return')
            while member.count_current_loan() > 0:
                title = input("Enter title or <ENTER> to end: ")
                if title:
                    try:
                        loan = member.search_loan_for(title)
                        if loan:
                            member.return_item(title, return_date)
                            print(f"Successfully returned {title}")
                    except LibraryException as e:
                        print(e)
                else:
                    break

            # Display member's info for verification
            print(member)

    def option_4(self):
        """
        """
        member = self.member_check()

        if member:
            if member.amount_owed == 0:
                print("There is no outstanding fines")
            else:
                try:
                    while True:
                        amount = input("Enter amount: ")
                        if amount.isdigit():
                            break
                        else:
                            print(f"{amount} is not a valid amount")
                    # Making the payment reflect for the member
                    change = member.pay(float(amount))
                    print(f"Sucessfully paid ${amount}. "
                          f"Current balance: ${member.amount_owed:.2f}")
                    if change:
                        print(f"Your change: ${change:.2f}")

                except LibraryPaymentException as pe:
                    print(pe)

            # Display member's info for verification
            print(member)

    # Print menu options
    def menu(self):
        print("Menu:")
        print("1. Borrow Item")
        print("2. Renew Item")
        print("3. Return Item")
        print("4. Pay Outstanding Balance")
        print("0. Exit")

        try:
            selected_option = input("Enter option: ")

            if int(selected_option) == 1:
                self.option_1()
            elif int(selected_option) == 2:
                self.option_2()
            elif int(selected_option) == 3:
                self.option_3()
            elif int(selected_option) == 4:
                self.option_4()
            elif int(selected_option) == 0:
                print("Program ends")
                exit()
            else:
                print("Invalid option")

        except ValueError:
            print(f"{selected_option} is not a valid menu option")


# Q3(D)(i)
def populated_items():
    """Informations to be populatd into Library object

    Items that are to be populated are Member objects, Items (Book & Media)
    Objects and ItemCopies objects.

    Return:
        members (list): List of Members
        items (list): List of Items (Books or Media)
        item_copies (dict): Dictionary containing information of number of copies
            per item.
    """

    # Creating the two member
    members = [Member('S123', 'John'), JuniorMember('J111', 'Mary')]

    # Creating the list of all the items in the library
    items = [Book('The Road to Forget', 2020, 35.00, ['Justin Grave', 'Tom Aplesson']),
             Media('Asia Food and Culture', 2019, 30.00),
             Book('Dark Knight', 2010, 29.00, ['Allyson Day']),
             Media('Powerpoint Presentation Tips', 2020, 15.00)]

    # Indicating no. of copies for items in the library
    item_copies = {'The Road to Forget': 2, 'Asia Food and Culture': 3,
                   'Dark Knight': 2, 'Powerpoint Presentation Tips': 2}

    return members, items, item_copies


# Q3(D)(ii)
def initialise_library(members, items, item_copies, library):
    """
    """

    print("*** Start initialising library ***\n")

    # Adding the items, item_copies, members into the library
    # Registering the members
    for member in members:
        library.register_member(member)

    # Adding the items to the library
    for item in items:
        library.add_item(item)

    # Adding the copies of the items to the library
    for item in items:
        copies = item_copies[item.title]
        for _ in range(copies):
            library.add_copy_item(item)

    # Key members_id and actual member object
    john = library.search_member('S123')
    mary = library.search_member('J111')

    # John borrows 4 items on 1 March 2021 and Mary borrows 1 item on 3 March 2021.
    item_copies_loaned = [(john, datetime(2021, 3, 1), [1, 3, 6, 8]),
                          (mary, datetime(2021, 3, 3), [9])]

    for record in item_copies_loaned:
        member = record[0]
        date_borrowed = record[1]
        copy_id_borrowed = record[2]

        for copy_id in copy_id_borrowed:
            item_copy = library.search_copy_item(copy_id)
            member.borrow_item(item_copy, date_borrowed)

    # Member data after Mary renews loan on 5 March 2021 and John returns
    # Copy Item 6, Dark Knight on 17 March 2021")

    # John returns 'Dark Knight on 17 March 2021'
    john.return_item('Dark Knight', datetime(2021, 3, 17))
    # Mary renews loan on 5 March 2021
    mary.renew('Powerpoint Presentation Tips', datetime(2021, 3, 5))

    # John data after paying fines and he receives change $1.50
    john.pay(2.00)

    # John data after borrowing copy item 6, Dark Knight again on 22 March 2021
    john.borrow_item(library.search_copy_item(6), datetime(2021, 3, 22))

    # Mary data after returning Powerpoint Presentation Tips on 17 March 2021
    mary.return_item("Powerpoint Presentation Tips", datetime(2021, 3, 17))

    print("*** Done initialising library ***\n")
    print("******* Library Test Data *******")
    print(library)
    print("******* Ends Library Test Data *******\n")

    return library


def main():

    # Instantiate the Library object
    library = Library()

    # Retrieving the information required to populate the Library object
    members, items, item_copies = populated_items()

    # Initialising the library with relevant information and sequence of events
    library = initialise_library(members, items, item_copies, library)
    # Generating menu with initialised Library object
    menu = LibraryApplication(library)

    while True:
        menu.menu()
        print()


if __name__ == '__main__':
    main()
