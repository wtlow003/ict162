import tkinter as tk
from tkinter import scrolledtext, IntVar, StringVar, ttk


class BookingManagementGUI:

    bookings = []

    def __init__(self, staycations: dict):
        self._staycations = staycations
        self._win = tk.Tk()
        self._win.title("Staycation and Booking Management (Low Wei Teck)")
        self.create_widgets()

        self._win.geometry("560x375")
        self._win.resizable(False, False)
        self._win.configure(bg="#ececec")

        self.start_application()
        self._win.mainloop()

    @staticmethod
    def label_widget(master, width, text, row, col):
        """
        """
        label = tk.Label(
            master=master, width=width, text=text, bg="#ececec", anchor='w', padx=5)
        label.grid(row=row, column=col)

    @staticmethod
    def entry_widget(master, width, textvar, row, col):
        """
        """
        entry = tk.Entry(master, width=width, borderwidth=0.5, highlightthickness=0,
                         disabledbackground="#ececec", textvariable=textvar)
        entry.grid(row=row, column=col)

        return entry

    def start_application(self):
        """
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
        """
        """
        button_pressed = self._radio_var.get()

        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety, self._nights_ety, self._cost_ety]}

        if button_pressed == '0':
            for linked in radio_buttons_links['0']:
                linked.config(state='normal')
            for unlinked in radio_buttons_links['1']:
                unlinked.delete(0, 'end')
                unlinked.config(state='disable')
        else:
            for linked in radio_buttons_links['1']:
                linked.config(state='normal')
            for unlinked in radio_buttons_links['0']:
                unlinked.delete(0, 'end')
                unlinked.config(state='disable')

    def create_widgets(self):
        """
        """
        style = ttk.Style()
        style.theme_use('aqua')

        last_radio_btn_pressed = None

        top_left = tk.Frame(self._win)
        top_right = tk.Frame(self._win)
        top_left.place(x=0, y=0)
        top_right.place(x=280, y=0)

        self._radio_var = StringVar()
        self._radio_var.set('')     # Deselect both radio buttons first
        self._booking_btn = tk.Radiobutton(
            top_left, text='Booking', variable=self._radio_var, value='0', bg="#ececec", command=self.select_radio_btn)
        self._staycation_btn = tk.Radiobutton(
            top_right, text='Staycation', variable=self._radio_var, value='1', bg="#ececec", command=self.select_radio_btn)

        self._booking_btn.grid(row=0, column=0, sticky="w")
        self._staycation_btn.grid(row=0, column=0, sticky="w")

        # Designing middle left entry text boxes
        middle_upper_left = tk.Frame(self._win)
        middle_upper_left.place(x=0, y=65)
        middle_upper_left.configure(bg="#ececec")

        # Label and entry widget for Staycation Code
        self.label_widget(middle_upper_left, 11, 'Staycation Code:', 0, 0)
        self._staycation_code_left = StringVar()
        self._staycation_code_left_ety = self.entry_widget(
            middle_upper_left, 17, self._staycation_code_left, 0, 1)

        # Label and entry widget for Customer Id
        self.label_widget(middle_upper_left, 11, 'Customer Id:', 1, 0)
        self._customer_id = StringVar()
        self._customer_id_ety = self.entry_widget(middle_upper_left, 17, self._customer_id, 1, 1)

        # Designing middle right entry text boxes
        middle_upper_right = tk.Frame(self._win)
        middle_upper_right.place(x=280, y=40)
        middle_upper_right.configure(bg="#ececec")

        # Label and entry widget for Staycation Code
        self.label_widget(middle_upper_right, 11, 'Staycation Code:', 0, 0)
        self._staycation_code_right = StringVar()
        self._staycation_code_right_ety = self.entry_widget(
            middle_upper_right, 17, self._staycation_code_right, 0, 1)

        # Label and entry widget for Hotel Name
        self.label_widget(middle_upper_right, 11, 'Hotel Name:', 1, 0)
        self._hotel_name = StringVar()
        self._hotel_name_ety = self.entry_widget(middle_upper_right, 17, self._hotel_name, 1, 1)

        # Label and entry widget for Nights
        self.label_widget(middle_upper_right, 11, 'Nights:', 2, 0)
        self._nights = StringVar()
        self._nights_ety = self.entry_widget(middle_upper_right, 17, self._nights, 2, 1)

        # Label and entry widget for Cost
        self.label_widget(middle_upper_right, 11, 'Cost: $', 3, 0)
        self._cost = StringVar()
        self._cost_ety = self.entry_widget(middle_upper_right, 17, self._cost, 3, 1)

        # Designing middle buttons
        middle_lower = tk.Frame(self._win)
        middle_lower.place(x=125, y=160)

        self._add_btn = ttk.Button(middle_lower, width=8, text='Add')
        self._add_btn.bind("<Button-1>", self.add_button)
        self._remove_btn = ttk.Button(middle_lower, width=8, text='Remove')
        self._remove_btn.bind("<Button-1>", self.remove_button)
        self._display_btn = ttk.Button(middle_lower, width=8, text='Display')
        self._display_btn.bind("<Button-1>", self.display_button)
        self._add_btn.pack(side='left')
        self._remove_btn.pack(side='left')
        self._display_btn.pack(side='left')

        bottom = tk.Frame(self._win)
        bottom.place(x=5, y=187.5)

        scrol_w, scrol_h = 77, 13
        self._scrolled_txt = scrolledtext.ScrolledText(
            bottom, width=scrol_w, height=scrol_h, wrap=tk.WORD, highlightthickness=0)
        self._scrolled_txt.grid(row=0, column=0, sticky="NSEW")
        self._scrolled_txt.config(state='disable')

    def check_entry(self, radio_button_pressed):

        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety, self._nights_ety, self._cost_ety]}

        empty = False

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

        radio_buttons_links = {'0': [self._staycation_code_left_ety, self._customer_id_ety],
                               '1': [self._staycation_code_right_ety, self._hotel_name_ety, self._nights_ety, self._cost_ety]}

        if radio_button_pressed == '0':
            for entry in radio_buttons_links['0']:
                entry.delete(0, tk.END)
        else:
            for entry in radio_buttons_links['1']:
                entry.delete(0, tk.END)

    def add_button(self, event=None):

        # Enable editing of scrolledtext for program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        if not radio_button_pressed:
            self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
        # Check if entries enabled are filled completely
        elif self.check_entry(radio_button_pressed):
            self._scrolled_txt.insert(tk.END, "Please complete all fields.\n")
        else:
            # If Booking is pressed
            if radio_button_pressed == '0':
                staycation_code = self._staycation_code_left.get()
                if staycation_code not in self._staycations:
                    self._scrolled_txt.insert(tk.END, "Invalid staycation code.\n")
                else:
                    member_id = self._customer_id_ety.get()
                    booking = [staycation_code, member_id]
                    type(self).bookings.append(booking)
                    print(type(self).bookings)
                    self.clear_entry(radio_button_pressed)
                    self._scrolled_txt.insert(tk.END, "Added a booking.\n")
            # If Staycation is pressed
            else:
                try:
                    staycation_code = self._staycation_code_right.get()
                    if staycation_code in self._staycations:
                        self._scrolled_txt.insert(
                            tk.END, "This code belongs to an existing staycation. Check the input.\n")
                    else:
                        hotel_name = self._hotel_name_ety.get()
                        nights = int(self._nights_ety.get())
                        cost = int(self._cost_ety.get())
                        self._staycations[staycation_code] = [hotel_name, nights, cost]
                        self.clear_entry(radio_button_pressed)
                        self._scrolled_txt.insert(tk.END, "Added a staycation.\n")
                except ValueError:
                    self._scrolled_txt.insert(tk.END, "Nights or Cost field must be Integer.\n")

        self._scrolled_txt.see(tk.END)
        self._scrolled_txt.config(state='disable')

    def remove_button(self, event=None):

        # Enable editing of scrolledtext for program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        if not radio_button_pressed:
            self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
        elif self.check_entry(radio_button_pressed):
            self._scrolled_txt.insert(tk.END, "Please complete all fields.\n")
        else:
            if radio_button_pressed == '0':
                staycation_code = self._staycation_code_left.get()
                member_id = self._customer_id_ety.get()
                if [staycation_code, member_id] not in type(self).bookings:
                    self._scrolled_txt.insert(
                        tk.END, "No matching booking to remove. Check the input.\n")
                else:
                    matching_idx = type(self).bookings.index([staycation_code, member_id])
                    type(self).bookings.pop(matching_idx)
                    self.clear_entry(radio_button_pressed)
                    self._scrolled_txt.insert(tk.END, "Removed a booking.\n")
            else:
                staycation_code = self._staycation_code_right.get()
                if staycation_code not in self._staycations:
                    self._scrolled_txt.insert(
                        tk.END, "This code does not belong to an existing staycation. Check the input.\n")
                else:
                    try:
                        hotel_name = self._hotel_name_ety.get()
                        nights = int(self._nights_ety.get())
                        cost = int(self._cost_ety.get())
                        match_code = self._staycations[staycation_code]

                        if match_code != [hotel_name, nights, cost]:
                            self._scrolled_txt.insert(
                                tk.END, "No matching staycation to remove. Check the input.\n")
                        else:
                            self._staycations.pop(staycation_code)
                            self.clear_entry(radio_button_pressed)
                            self._scrolled_txt.insert(tk.END, "Removed a staycation.\n")
                    except ValueError:
                        self._scrolled_txt.insert(tk.END, "Nights or Cost field must be Integer.\n")

        self._scrolled_txt.see(tk.END)
        self._scrolled_txt.config(state='disable')

    def display_button(self, event=None):

        # Enable editing of scolledtext of program to input data
        self._scrolled_txt.config(state='normal')
        radio_button_pressed = self._radio_var.get()

        if not radio_button_pressed:
            self._scrolled_txt.insert(tk.END, "Select either Booking or Staycation first.\n")
        elif radio_button_pressed == '0':
            if not type(self).bookings:
                self._scrolled_txt.insert(tk.END, "No booking currently.\n")
            else:
                text = '\n'.join(
                    [f"Booking {idx + 1}: {val[0]} {val[1]}" for idx, val in enumerate(type(self).bookings)])
                self._scrolled_txt.insert(tk.END, text + '\n')
        else:
            if not self._staycations:
                self._scrolled_txt.insert(tk.END, "No staycations currently.\n")
            else:
                text = '\n'.join(
                    [f"Staycation code: {key} {val[0]} {val[1]} nights ${val[2]}" for key, val in self._staycations.items()])
                self._scrolled_txt.insert(tk.END, text + '\n')

        self._scrolled_txt.see(tk.END)
        self._scrolled_txt.config(state='disable')


if __name__ == '__main__':
    staycations = {'GM1': ['Grand Marina', 1, 238],
                   'GM2': ['Grand Marina', 2, 398],
                   'HB1': ['Hotel Bugis', 1, 168],
                   'HB2': ['Hotel Bugis', 2, 300],
                   'HB3': ['Hotel Bugis', 3, 400]}

    BookingManagementGUI(staycations)
