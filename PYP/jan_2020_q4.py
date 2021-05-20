# JAN 2020 Q4
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class StatsGui:
    def __init__(self):
        self._numbers = []
        self.win = tk.Tk()
        self.win.resizable(False, False)
        self.win.title("Statistics")
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        dataFrame = ttk.Frame(self.win)
        dataFrame.grid(column=0, row=0)

        inputDataFrame = ttk.Frame(dataFrame)
        p1_lbl = ttk.Label(inputDataFrame, text="Number:")
        p1_lbl.pack(side=tk.LEFT)

        self.numValue = tk.StringVar()
        self.numValue_Ety = ttk.Entry(inputDataFrame, width=18,
                                    textvariable=self.numValue)
        self.numValue_Ety.pack(side=tk.LEFT)
        inputDataFrame.grid(column = 0, row = 0)

        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=0, row=1)

        self.add_btn = ttk.Button(actionFrame, text="Add A Number")
        self.add_btn.pack(side = tk.LEFT)
        self.add_btn.bind("<Button>", self.add_number)

        self.statistics_btn = ttk.Button(actionFrame, text="Get Statistics")
        self.statistics_btn.pack(side = tk.LEFT)
        self.statistics_btn.bind("<Button>", self.get_statistics)

        outputFrame = ttk.Frame(self.win)
        outputFrame.grid(column=0, row=2, columnspan=2)

        self.output = ScrolledText(outputFrame, width=40, height=10,
                                wrap=tk.WORD)
        self.output.grid(column=0, row=0, sticky='WE', columnspan=2)

    def add_number(self, event):
        # retrieving the number in the entry box
        add_num = self.numValue.get()
        # enable the scrolled text for insertion
        self.output.config(state='normal')

        # try and except block to catch invalid values
        try:
            self._numbers.append(int(add_num))
            self.output.insert(tk.END, f"Added {add_num} in the list.\n")
        except ValueError:
            self.output.insert(tk.END, f"Please check if empty or invalid value is entered.\n")

        # ckear the entry box
        self.numValue_Ety.delete(0, tk.END)
        # disabled meddling with scrolled text
        self.output.config(state='disable')

    def get_statistics(self, event):
        curr_list = self._numbers
        # enable scrolled text for insertion
        self.output.config(state='normal')

        # the current list is empty
        if not curr_list:
            self.output.insert(tk.END,
                               f"Numbers in list: {curr_list}\n"
                               "No statistics to produce.\n")
        else:
            maximum = max(curr_list)
            minimum = min(curr_list)
            total = sum(curr_list)
            count = len(curr_list)
            average = total / count
            self.output.insert(tk.END,
                               f"\nNumbers in list: {curr_list}\n"
                               f"Maximum: {maximum}\n"
                               f"Minimum: {minimum}\n"
                               f"Total: {total}\n"
                               f"Count of numbers: {count}\n"
                               f"Average: {average:.2f}\n")
        # disable the scroll text for meddling
        self.output.config(state='disable')


if __name__ == '__main__':
    StatsGui()