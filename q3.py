# Q3(A)
from datetime import datetime
from q2 import Book, Media, Loan, ItemCopy, Item


class LibraryException(Exception):
    """Exception class for exceptions raised in Library application.
    """


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

        Upon returning the item, the fines is also recorded if any fines are
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
        matched_loans.item_copy.available = True    # update the item copy back to available
        # retrieving fines, if any
        fines_incurred = matched_loans.get_fines()
        if fines_incurred:
            self._amount_owed += fines_incurred     # fines added to `amount_owed`
        return True

    def pay(self, amount: float) -> float:
        """Method to allow members to pay their outstanding fines

        The `pay` method raises certain exceptions as follows:
            1. The `amount` is not more than 0

        Return:
            change (float): change if the amount paid exceed amount owed, default
            to [0]
        """
        if amount < 0:
            raise LibraryPaymentException(amount,
                                          f"You owed ${self._amount_owed}. "
                                          "Please pay an amount more than $0.")
        # if you paid < owed, change = 0
        # if paid == owed, change = 0
        # if paid > owed, change > 0
        change = amount - self._amount_owed if amount > self._amount_owed else 0
        # making the adjustment to outstanding fines
        self._amount_owed -= amount
        return change

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
        """Add item to `_items` if item's title does not exist
        """
        if item.title not in self._items.keys():
            self._items[item.title] = item
            return True
        return False

    def add_copy_item(self, item: Item) -> None:
        """Creates a copy item and adds to `_copy_items`
        """
        copy_item = ItemCopy(item)
        self._copy_items.append(copy_item)

    def register_member(self, member: Member) -> bool:
        """Add a member to `_members` if member id does not exist
        """
        if member.member_id not in self._members:
            self._members[member.member_id] = member
            return True
        return False

    def remove_member(self, member_id: str) -> Member:
        """Remove a member from `_members` based on the `member_id`
        """
        # if member exist remove and return the member, else return None
        return self._members.pop(member_id, None)

    def search_member(self, member_id: str) -> Member:
        """Search a member based on `member_id` from `_members``
        """
        if member_id in self._members:
            return self._members[member_id]
        return None

    def search_copy_item(self, copy_id: int) -> ItemCopy:
        """Search a copy item based on `copy_id` from `_copy_items`
        """
        matched = [copy for copy in self._copy_items if copy.copy_id == copy_id]
        # empty list -> False, list with element -> True
        if matched:
            return matched[0]
        return False

    # TODO: check logic and refactoring
    def get_available_copy_items(self) -> list:
        available = [copy for copy in self._copy_items if copy.available is True]
        return available

    def copy_item_str(self, copy_item_list: list = None) -> str:
        if copy_item_list:
            copy_items = '\n'.join([str(copy) for copy in copy_item_list])
        else:
            copy_items = '\n'.join([str(copy) for copy in self._copy_items])
        return (f"{copy_items}")

    def member_str(self) -> str:
        members = '\n'.join([str(mem) for mem in self._members.values()])
        return ("Members\n"
                f"{members}")

    def item_str(self) -> str:
        items = '\n'.join([str(item) for item in self._items.values()])
        return ("Items\n"
                f"{items}\n")

    def __str__(self) -> str:
        return (f"{self.item_str()}"
                f"\n{self.copy_item_str()}"
                f"\n{self.member_str()}")


class LibraryApplication:
    """
    """

    def __init__(self, library: Library):
        self._library = library

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

    def option_1(self):
        """Allow users to borrow items through available copy ids
        """
        member_id = input("Enter member id: ")

        # Check if member id is valid
        member = self._library.search_member(member_id.upper())
        if member is None:
            print("Invalid member id")
        else:
            print(
                f"Current number of loans: {member.count_current_loan()} Quota: {member.get_loan_quota()}")

            # Loop until member enters correct date format for borrowing
            while True:
                borrow_date = input("Enter borrow date in dd/mm/yyyy: ")
                date_format = "%d/%m/%Y"
                try:
                    borrow_date = datetime.strptime(borrow_date, date_format)
                    break
                except ValueError:
                    print(f"{borrow_date} is not in the format dd/mm/yyyy")

            while member.count_current_loan() < member.get_loan_quota():
                # Display all the available items in the library
                available_items = self._library.get_available_copy_items()
                available_items_ids = [avail.copy_id for avail in available_items]
                print(self._library.copy_item_str(available_items))

                # Get user option for items to borrow, else exit current menu option
                copy_item_choice = input("Enter the copy id or 0 to end: ")

                if int(copy_item_choice) in available_items_ids:
                    item_copy = self._library.search_copy_item(int(copy_item_choice))
                    member.borrow_item(item_copy, borrow_date)
                elif copy_item_choice == '0':
                    break
                else:
                    print("Invalid copy id - does not match available items")

    def option_2(self):
        """Allow users to renew items through title
        """
        member_id = input("Enter member id: ")
        title = input("Enter title: ")

        # Check if member id is valid
        member = self._library.search_member(member_id.upper())
        if member is None:
            print("Invalid member id")
        else:
            while True:
                renew_date = input("Enter renew date in dd/mm/yyyy: ")
                date_format = "%d/%m/%Y"
                try:
                    renew_date = datetime.strptime(renew_date, date_format)
                    break
                except ValueError:
                    print(f"{renew_date} is not in the format dd/mm/yyyy")

            # TODO: check if title exists within the member's loan
            member = self._library.search_member(member_id)
            loan = member.search_loan_for(title)
            # check if the loan is past or present loan
            if loan is not None:
                if loan.return_date is None:
                    print(f"Item has been returned on {loan.return_date}")
                else:
                    print("Sucessfully renewed {title}")
            print("There is no loan recorded for {title}")


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
    john = Member('S123', 'John')
    mary = JuniorMember('J111', 'Mary')
    members = [john, mary]

    # Creating the items in the library
    item_1 = Book('The Road to Forget', 2020, 35.00, ['Justin Grave',
                                                      'Tom Aplesson'])
    item_2 = Media('Asia Food and Culture', 2019, 30.00)
    item_3 = Book('Dark Knight', 2010, 29.00, ['Allyson Day'])
    item_4 = Media('Powerpoint Presentation Tips', 2020, 15.00)
    # Creating the list of all the items
    items = [item_1, item_2, item_3, item_4]

    # Indicating no. of copies for items in the library
    item_copies = {'The Road to Forget': 2, 'Asia Food and Culture': 3,
                   'Dark Knight': 2, 'Powerpoint Presentation Tips': 2}

    return members, items, item_copies


def initalise_library(library):

    # Key members_id and actual member object
    john_id = 'S123'
    mary_id = 'J111'

    john = library.search_member(john_id)
    mary = library.search_member(mary_id)

    # print("John borrows 4 items on 1 March 2021 and Mary borrows 1 item on 3 March 2021.")
    item_copies_loaned = [(john_id, datetime(2021, 3, 1), [1, 3, 6, 8]),
                          (mary_id, datetime(2021, 3, 3), [9])]    # item copies loaned by john and mary

    for loan in item_copies_loaned:
        member_id = loan[0]
        date_borrowed = loan[1]
        copy_id_borrowed = loan[2]
        member = library.search_member(member_id)     # search by member id

        for copy_id in copy_id_borrowed:
            item_copy = library.search_copy_item(copy_id)
            member.borrow_item(item_copy, date_borrowed)

    # print(f"{library}\n")

    # print("Member data after Mary renews loan on 5 March 2021 and John returns Copy Item 6, "
    #       "Dark Knight on 17 March 2021")

    # John returns 'Dark Knight on 17 March 2021'
    item_copy = library.search_copy_item(6)
    john.return_item(item_copy.item.title, datetime(2021, 3, 17))
    mary.renew('Powerpoint Presentation Tips', datetime(2021, 3, 5))
    # TODO: remove this test later on
    # mary.renew('Hello Panda', datetime(2021, 3, 5))
    # print(f"{library.member_str()}\n")

    # print("John data after paying fines and he receives change $1.50")
    # TODO: ensure that member class's `pay` can work
    john.pay(2.00)
    # print(john)

    # print("John data after borrowing copy item 6, Dark Knight again on 22 March 2021")
    item_copy = library.search_copy_item(6)
    john.borrow_item(item_copy, datetime(2021, 3, 22))
    # print(john)

    # print("Mary data after returning Powerpoint Presentation Tips on 17 March 2021")
    item_copy = library.search_copy_item(9)
    mary.return_item(item_copy.item.title, datetime(2021, 3, 17))

    # print(mary)
    # print("*** Done initialising library ***\n")
    #
    # print("******* Library Test Data")
    # print(library)

    return library


def main():

    # TODO: Temp solutions

    # Instantiate the library object
    library = Library()

    # Retrieving the information required to populate the Library class
    members, items, item_copies = populated_items()

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

    library = initalise_library(library)
    menu = LibraryApplication(library)

    while True:
        menu.menu()
        print()


if __name__ == '__main__':
    main()
