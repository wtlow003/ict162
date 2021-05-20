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

        self.statistics_btn = ttk.Button(actionFrame, text="Get Statistics")
        self.statistics_btn.pack(side = tk.LEFT)

        outputFrame = ttk.Frame(self.win)
        outputFrame.grid(column=0, row=2, columnspan=2)

        self.output = ScrolledText(outputFrame, width=40, height=10,
                                wrap=tk.WORD)
        self.output.grid(column=0, row=0, sticky='WE', columnspan=2)


if __name__ == '__main__':
    StatsGui()