from datetime import datetime
from q2 import Item, Book, Media, Loan, ItemCopy
from TMA01_q3 import Member


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
        copy_items = '\n'.join([str(copy) for copy in self._copy_items])
        return ("Copy Items\n"
                f"{copy_items}\n")

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
    mary = Member('J111', 'Mary')
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


def main():
    """Populate the Library object based on the sequence of event in the TMA.
    """
    print("*** Start initialising library ***")

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

    # Key members_id and actual member object
    john_id = 'S123'
    mary_id = 'J111'

    john = library.search_member(john_id)
    mary = library.search_member(mary_id)

    print("John borrows 4 items on 1 March 2021 and Mary borrows 1 item on 3 March 2021.")
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

    print(f"{library}\n")

    print("Member data after Mary renews loan on 5 March 2021 and John returns Copy Item 6, "
          "Dark Knight on 17 March 2021")

    # John returns 'Dark Knight on 17 March 2021'
    item_copy = library.search_copy_item(6)
    john.return_item(item_copy.item.title, datetime(2021, 3, 17))
    item_copy.available = True
    mary.renew('Powerpoint Presentation Tips', datetime(2021, 3, 5))
    # TODO: remove this test later on
    # mary.renew('Hello Panda', datetime(2021, 3, 5))
    print(f"{library.member_str()}\n")

    print("John data after paying fines and he receives change $1.50")
    # TODO: ensure that member class's `pay` can work
    john.pay(2.00)
    print(john)

    print("John data after borrowing copy item 6, Dark Knight again on 22 March 2021")
    item_copy = library.search_copy_item(6)
    john.borrow_item(item_copy, datetime(2021, 3, 22))
    print(john)

    print("Mary data after returning Powerpoint Presentation Tips on 17 March 2021")
    item_copy = library.search_copy_item(9)
    mary.return_item('Powerpoint Presentation Tips', datetime(2021, 3, 17))
    item_copy.available = True
    print(mary)
    print("*** Done initialising library ***\n")

    print("******* Library Test Data")
    print(library)


if __name__ == '__main__':
    main()
