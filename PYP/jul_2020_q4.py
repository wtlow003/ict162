# JUL 2020 Q4
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

class TourGui:
    def __init__(self):
        self._numberOfPax = 5
        self.win = tk.Tk()
        self.win.resizable(False, False)
        self.win.title("Tour ABC")
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        outputFrame = ttk.Frame(self.win)
        outputFrame.grid(column=0, row=0, columnspan=2)
        self.output = ScrolledText(outputFrame, width=35, height=6,
                                   wrap=tk.WORD)
        self.output.grid(column=0, row=0, sticky='WE')

        inputDataFrame = ttk.Frame(self.win)
        p1_lbl = ttk.Label(inputDataFrame, text="Number of Pax:")
        p1_lbl.pack(side=tk.LEFT)

        self.numValue = tk.StringVar()
        self.numValue_Ety = ttk.Entry(inputDataFrame, width=18,
                                      textvariable=self.numValue)
        self.numValue_Ety.pack(side=tk.LEFT)
        inputDataFrame.grid(column = 0, row = 1, columnspan=2)

        actionFrame = ttk.Frame(self.win)
        actionFrame.grid(column=0, row=2, columnspan=2)
        self.add_btn = ttk.Button(actionFrame, text="Add Pax")
        self.add_btn.pack(side = tk.LEFT)
        self.remove_btn = ttk.Button(actionFrame, text="Remove Pax")
        self.remove_btn.pack(side = tk.LEFT)


if __name__ == '__main__':
    TourGui()