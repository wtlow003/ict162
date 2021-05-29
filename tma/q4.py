"""
Created on 04 Apr 2021

@author: Low Wei Teck

22 Apr 2021: Started adding integrity checks, added .strip() to prevent whitespaces.
    Added .lower() -> then .upper()/.title() before checks/inserts

"""


import tkinter as tk
from tkinter import scrolledtext, StringVar, ttk, messagebox


class BookingManagementGUI:
    """A class to represent the GUI of Booking Management System.

    The GUI allows uses to interact with to add, remove, display respective
    booking and staycation information.

    Attributes:
        bookings (list): A list to keep track of the bookings for staycation
            that occured.

    Example:
        >>> BookingManagementGUI(staycations: dict)

    """
    bookings = []

    def __init__(self, staycations: dict):
        self._staycations = staycations
        self._win = tk.Tk()

        # Setting properties for top container of the GUI
        self._win.title("Staycation and Booking Management (Low Wei Teck)")
        self._win.geometry("560x375")
        self._win.resizable(False, False)
        self._win.config(bg="#ececec")

        # Creating all widgets
        self.create_widgets()
        # Settting GUI initial behaviour
        self.start_application()
        # Get `self._win` into a loop
        self._win.mainloop()

    @staticmethod
    def label_widget(master, width, text, row, col):
        """Method not bound to the object, to create a label widget for the GUI.

        Args:
            master (tkinter.Frame): Rectangular area that groups the Label Widget
            width (int): Width of the intended Label Widget
            text (str): Text to be displayed for the Label Widget
            row (int): On the `master` grid, which position on the row to be placed
            col (int):  On the `master` grid, which position on the column to be placed

        Returns:
            label (tkinter.Label): Returns Label Widget that display text for the
                Entry Widget associated with

        """

        label = tk.Label(
            master=master, width=width, text=text, bg="#ececec", anchor='w', padx=5)
        label.grid(row=row, column=col)

        return label

    @staticmethod
    def entry_widget(master, width, textvar, row, col):
        """Method not bound to the object, to create a entry widget for the GUI.

        Args:
            master (tkinter.Frame): Rectangular area that groups the Entry Widget
            width (int): Width of the intended Entry Widget
            textvar (tkinter.StringVar): Creating string variable as set and accessed
                by the Entry Widget
            row (int): On the `master` grid, which positon on the row to be placed
            col (int): On the `master` grid, which position on the column to be placed

        Returns:
            entry (tkinter.Entry): Returns Entry Widget that accept single-line
                text strings from users

        """

        entry = tk.Entry(master, width=width, borderwidth=0.5, highlightthickness=0,
                         disabledbackground="#ececec", textvariable=textvar)
        entry.grid(row=row, column=col)

        return entry

    def start_application(self):
        """Method to ensure that when starting the application, all Entry Widgets
            are disabled to prevent entry until radio buttons are pressed.

        """

        entry_widgets = [self._staycation_code_left_ety,
                         self._staycation_code_right_ety,
                         self._customer_id_ety,
                         self._hotel_name_ety,
                         self._nights_ety,
                         self._cost_ety]

        for e in entry_widgets:
            e.config(state='disabled')

    def select_radio_btn(self):
        """Method to toggle selected Entry Widgets on either side (left/right)
            based on the radio button pressed (Bookings/Staycations).

        The associated Entry Widgets are tied to the respective radio button's value,
        `self._booking_btn` = '0' and `self._staycation_btn` = '1'. When either
        buttons are selected, the opposite Entry Widgets (e.g., for '1'), '0' will be disabled and
        greyed out. The previously inputs given in the Entry Widgets, will be also
        be cleared when another radio button is pressed.

        """

        # Checking on which radio button is pressed.
        button_pressed = self._radio_var.get()
        # Radio button and their respective associated Entry Widgets
        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety,
                                     self._nights_ety, self._cost_ety]}

        # When booking radio button is pressed
        if button_pressed == '0':
            for linked in radio_buttons_links['0']:
                # Enable the Entry Widgets associated with Radio Button '0'
                linked.config(state='normal')
            for unlinked in radio_buttons_links['1']:
                # Clear existing inputs in Entry Widgets for Radio Button '1'
                unlinked.delete(0, 'end')
                # Disable inputs for Entry Widgets for Radio Button '1'
                unlinked.config(state='disable')
        # when staycation radio button is pressed
        else:
            for linked in radio_buttons_links['1']:
                # Enable the Entry Widgets associated with Radio Button '1'
                linked.config(state='normal')
            for unlinked in radio_buttons_links['0']:
                # Clear existing inputs in Entry Widgets for Radio Button '0'
                unlinked.delete(0, 'end')
                # Disable inputs for Entry Widgets for Radio Button '0'
                unlinked.config(state='disable')

    def check_entry(self, radio_button_pressed):
        """Method to check if all Entry Widgets associated with the radio button
            pressed is completely filled.

        Uses the `radio_button_links` dictionary to determine which Entry Widgets
        to check based on the radio button pressed.

        Args:
            radio_button_pressed: Returned value of the radio button pressed,
                where '0' == 'self._booking_btn', '1' == 'self._staycation_btn'

        Returns:
            empty (bool): False if all Entry Widgets are filled, True if otherwise.

        """

        # Dictionary indiciating what entry widgets to tied to which radio button
        # Booking == '0', Staycation == '1'
        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety,
                                     self._nights_ety, self._cost_ety]}

        empty = False

        # Check if each entry widget is filled, return empty if any unfilled
        if radio_button_pressed == '0':
            for entry in radio_buttons_links['0']:
                if not entry.get():
                    empty = True
        else:
            for entry in radio_buttons_links['1']:
                if not entry.get():
                    empty = True

        return empty

    def clear_entry(self, radio_button_pressed):
        """Method to clear inputs in the Entry Widgets when action is fulfilled,
            e.g., adding or removing bookings or staycations.

        """

        # Booking == '0', Staycation == '1'
        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety,
                                     self._nights_ety, self._cost_ety]}

        if radio_button_pressed == '0':
            for entry in radio_buttons_links['0']:
                entry.delete(0, tk.END)
        else:
            for entry in radio_buttons_links['1']:
                entry.delete(0, tk.END)

    def add_button(self):
        """Method to call for when `self._add_btn` is pressed

        Performs action when `self._add_btn` is pressed depending on the radio
        button toggled. The method adds booking or staycation when all the
        Entry Widgets are completed filled.

        Raises:
            ValueError: When `self._cost_ety` or `self._nights_ety` is not inputted
                with integer values

        """

        # Enable editing of scrolledtext for program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        # Error message if no radio button pressed
        if not radio_button_pressed:
            # If we want to write message in the scroll text
            # We can use the code below
            # self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
            # However, a message box would bring more attention to the need
            # to press a radio button first.
            messagebox.showwarning(
                "Error", "Select either Booking or Staycation first.")
        # Check if entries enabled are filled completely
        elif self.check_entry(radio_button_pressed):
            self._scrolled_txt.insert(tk.END, "Please complete all fields.\n")
        else:
            # If Booking is pressed
            if radio_button_pressed == '0':
                staycation_code = self._staycation_code_left.get().lower().strip()
                # If booking is not associated with any existing staycation hotels
                if staycation_code.upper() not in self._staycations:
                    self._scrolled_txt.insert(tk.END, "Invalid staycation code.\n")
                else:
                    member_id = self._customer_id_ety.get().lower().strip()
                    booking = [staycation_code.upper(), member_id.upper()]
                    type(self).bookings.append(booking)
                    self.clear_entry(radio_button_pressed)  # clear entry after inserted
                    self._scrolled_txt.insert(tk.END, "Added a booking.\n")
            # If Staycation is pressed
            else:
                try:
                    staycation_code = self._staycation_code_right.get().lower().strip()
                    # if staycation code exists, you cant add the same code
                    if staycation_code.upper() in self._staycations:
                        self._scrolled_txt.insert(
                            tk.END, "This code belongs to an existing staycation. Check the input.\n")
                    else:
                        hotel_name = self._hotel_name_ety.get().lower().strip()
                        nights = int(self._nights_ety.get())
                        cost = int(self._cost_ety.get())
                        # add staycation to the staycation dict
                        self._staycations[staycation_code.upper()] = [
                            hotel_name.title(), nights, cost]
                        self.clear_entry(radio_button_pressed)  # clear entry after inserted
                        self._scrolled_txt.insert(tk.END, "Added a staycation.\n")
                except ValueError:
                    self._scrolled_txt.insert(tk.END, "Nights or Cost field must be Integer.\n")

        # Scrolling to the end of the text displayed
        self._scrolled_txt.see(tk.END)
        # Disabled the scroll text to prevent users from messing with the display
        self._scrolled_txt.config(state='disable')

    def remove_button(self):
        """Method to call for when `self._remove_btn` is pressed

        Performs action when `self._remove_btn` is pressed depending on the radio
        button toggled. The method removes existing booking or staycation when all the
        Entry Widgets are completed filled.

        Raises:
            ValueError: When `self._cost_ety` or `self._nights_ety` is not inputted
                with integer values

        """

        # Enable editing of scrolledtext for program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        if not radio_button_pressed:
            # self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
            messagebox.showwarning(
                "Error", "Select either Booking or Staycation first.")
        elif self.check_entry(radio_button_pressed):
            self._scrolled_txt.insert(tk.END, "Please complete all fields.\n")
        else:
            # Booking selected
            if radio_button_pressed == '0':
                staycation_code = self._staycation_code_left.get().lower().strip()
                member_id = self._customer_id_ety.get().lower().strip()
                # Check if booking exists
                if [staycation_code.upper(), member_id.upper()] not in type(self).bookings:
                    self._scrolled_txt.insert(
                        tk.END, "No matching booking to remove. Check the input.\n")
                else:
                    # if exists, remove the booking
                    matching_idx = type(self).bookings.index(
                        [staycation_code.upper(), member_id.upper()])
                    type(self).bookings.pop(matching_idx)
                    self.clear_entry(radio_button_pressed)  # clear entry after done
                    self._scrolled_txt.insert(tk.END, "Removed a booking.\n")
            # Staycation selected
            else:
                staycation_code = self._staycation_code_right.get().lower().strip()
                # check if staycation exists
                if staycation_code.upper() not in self._staycations:
                    self._scrolled_txt.insert(
                        tk.END, "This code does not belong to an existing staycation. Check the input.\n")
                else:
                    try:
                        hotel_name = self._hotel_name_ety.get().lower().strip()
                        nights = int(self._nights_ety.get())
                        cost = int(self._cost_ety.get())
                        matched = self._staycations[staycation_code.upper()]
                        # check if completed entry matched
                        if matched != [hotel_name.title(), nights, cost]:
                            self._scrolled_txt.insert(
                                tk.END, "No matching staycation to remove. Check the input.\n")
                        else:
                            self._staycations.pop(staycation_code.upper())
                            self.clear_entry(radio_button_pressed)  # clear entry after done
                            self._scrolled_txt.insert(tk.END, "Removed a staycation.\n")
                    except ValueError:
                        self._scrolled_txt.insert(tk.END,
                                                  "Nights or Cost field must be Integer.\n")

        # Scrolling to the end of the text displayed
        self._scrolled_txt.see(tk.END)
        # Disabled the scroll text to prevent users from messing with the display
        self._scrolled_txt.config(state='disable')

    def display_button(self):
        """Method to call for when `self._display_btn` is pressed

        Performs action when `self._display_btn` is pressed depending on the radio
        button toggled. The method displays all bookings or staycations.

        """

        # Enable editing of scolledtext of program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        if not radio_button_pressed:
            # self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
            messagebox.showwarning(
                "Error", "Select either Booking or Staycation first.")
        # Booking selected
        elif radio_button_pressed == '0':
            if not type(self).bookings:
                self._scrolled_txt.insert(tk.END, "No booking currently.\n")
            else:
                # display format if booking exists
                text = '\n'.join(
                    [f"Booking {idx + 1}: {val[0]} {val[1]}"
                     for idx, val in enumerate(type(self).bookings)])
                self._scrolled_txt.insert(tk.END, text + '\n')
        # Staycation selected
        else:
            if not self._staycations:
                self._scrolled_txt.insert(tk.END, "No staycations currently.\n")
            else:
                # display format if staycation exists
                text = '\n'.join(
                    [f"Staycation code: {key} {val[0]} {val[1]} {'nights' if val[1] > 1 else 'night'} "
                     f"${val[2]}" for key, val in self._staycations.items()])
                self._scrolled_txt.insert(tk.END, text + '\n')

        # Scrolling to the end of the text displayed
        self._scrolled_txt.see(tk.END)
        # Disabled the scroll text to prevent users from messing with the display
        self._scrolled_txt.config(state='disable')

    def create_widgets(self):
        """Method to create all widgets required for the booking management GUI"""

        ##### Desigining top radio buttons #####
        top_left = tk.Frame(self._win)
        top_right = tk.Frame(self._win)
        top_left.place(x=0, y=0)
        top_right.place(x=280, y=0)

        self._radio_var = StringVar()
        self._radio_var.set('')     # Deselect both radio buttons first
        # Booking == '0' and Staycation == '1'
        self._booking_btn = tk.Radiobutton(
            top_left, text='Booking', variable=self._radio_var,
            value='0', bg="#ececec", command=self.select_radio_btn)
        self._staycation_btn = tk.Radiobutton(
            top_right, text='Staycation', variable=self._radio_var,
            value='1', bg="#ececec", command=self.select_radio_btn)

        self._booking_btn.grid(row=0, column=0, sticky="w")
        self._staycation_btn.grid(row=0, column=0, sticky="w")

        ##### Designing middle left entry text boxes #####
        middle_upper_left = tk.Frame(self._win)
        middle_upper_left.place(x=0, y=65)
        middle_upper_left.configure(bg="#ececec")

        # Label and entry widget for Staycation Code
        self._staycation_code_left_lbl = self.label_widget(
            middle_upper_left, 11, 'Staycation Code:', 0, 0)
        self._staycation_code_left = StringVar()
        self._staycation_code_left_ety = self.entry_widget(
            middle_upper_left, 17, self._staycation_code_left, 0, 1)

        # Label and entry widget for Customer Id
        self._customer_id_lbl = self.label_widget(middle_upper_left, 11, 'Customer Id:', 1, 0)
        self._customer_id = StringVar()
        self._customer_id_ety = self.entry_widget(middle_upper_left, 17, self._customer_id, 1, 1)

        ##### Designing middle right entry text boxes #####
        middle_upper_right = tk.Frame(self._win)
        middle_upper_right.place(x=280, y=40)
        middle_upper_right.configure(bg="#ececec")

        # Label and entry widget for Staycation Code
        self._staycation_code_right_lbl = self.label_widget(
            middle_upper_right, 11, 'Staycation Code:', 0, 0)
        self._staycation_code_right = StringVar()
        self._staycation_code_right_ety = self.entry_widget(
            middle_upper_right, 17, self._staycation_code_right, 0, 1)

        # Label and entry widget for Hotel Name
        self._hotel_name_lbl = self.label_widget(middle_upper_right, 11, 'Hotel Name:', 1, 0)
        self._hotel_name = StringVar()
        self._hotel_name_ety = self.entry_widget(middle_upper_right, 17, self._hotel_name, 1, 1)

        # Label and entry widget for Nights
        self._nights_lbl = self.label_widget(middle_upper_right, 11, 'Nights:', 2, 0)
        self._nights = StringVar()
        self._nights_ety = self.entry_widget(middle_upper_right, 17, self._nights, 2, 1)

        # Label and entry widget for Cost
        self._cost_lbl = self.label_widget(middle_upper_right, 11, 'Cost: $', 3, 0)
        self._cost = StringVar()
        self._cost_ety = self.entry_widget(middle_upper_right, 17, self._cost, 3, 1)

        ##### Designing middle buttons #####
        middle_lower = tk.Frame(self._win)
        middle_lower.place(x=125, y=160)

        # Creating Add, Remove, Remove buttons and binding them to left mouse click
        self._add_btn = ttk.Button(middle_lower, width=8, text='Add', command=self.add_button)
        self._remove_btn = ttk.Button(
            middle_lower, width=8, text='Remove', command=self.remove_button)
        self._display_btn = ttk.Button(
            middle_lower, width=8, text='Display', command=self.display_button)

        # Placement of the buttons
        self._add_btn.pack(side='left')
        self._remove_btn.pack(side='left')
        self._display_btn.pack(side='left')

        ##### Designing bottom scrolled text #####
        bottom = tk.Frame(self._win)
        bottom.place(x=5, y=187.5)

        # Creating Scrolled Text to display the results given inputs.
        scrol_w, scrol_h = 77, 13   # Setting scrolled text size
        self._scrolled_txt = scrolledtext.ScrolledText(
            bottom, width=scrol_w, height=scrol_h, wrap=tk.WORD, highlightthickness=0)
        self._scrolled_txt.grid(row=0, column=0, sticky="NSEW")
        # Disable scrolled text to prevent users from typing at the start
        # Only activating scrolled text when display of information is required
        self._scrolled_txt.config(state='disable')


def main():
    """Instantiate and initialize the Booking Management GUI"""
    staycations = {'GM1': ['Grand Marina', 1, 238],
                   'GM2': ['Grand Marina', 2, 398],
                   'HB1': ['Hotel Bugis', 1, 168],
                   'HB2': ['Hotel Bugis', 2, 300],
                   'HB3': ['Hotel Bugis', 3, 400]}

    BookingManagementGUI(staycations)


if __name__ == '__main__':
    main()
