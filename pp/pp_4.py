from tkinter import *
from tkinter.scrolledtext import ScrolledText
from pp_1 import Instructor


class TrainingProviderGUI:
    def __init__(self):
        self._instructors = {}
        self._tk = Tk()
        self._tk.geometry("270x200")
        self._tk.title("Training Provider")
        self.createWidgets()
        self._tk.mainloop()

    def createWidgets(self):
        inputFrame = Frame(self._tk)
        lblEmail = Label(inputFrame, text="Email: ")
        self.lblEmail_var = StringVar()
        self._tbxEmail = Entry(inputFrame, width=15, textvariable=self.lblEmail_var)
        lblEmail.grid(row=0, column=0, sticky=W)
        self._tbxEmail.grid(row=0, column=1, sticky=W)

        lblName = Label(inputFrame, text="Name: ")
        self.lblName_var = StringVar()
        self._tbxName = Entry(inputFrame, width=25, textvariable=self.lblName_var)
        lblName.grid(row=1, column=0, sticky=W)
        self._tbxName.grid(row=1, column=1, sticky=W)

        lblRate = Label(inputFrame, text="Rate per day: ")
        self.lblRate_var = StringVar()
        self._tbxRate = Entry(inputFrame, width=10, textvariable=self.lblRate_var)
        lblRate.grid(row=2, column=0, sticky=W)
        self._tbxRate.grid(row=2, column=1, sticky=W)

        inputFrame.grid(row=0, column=0)
        buttonFrame = Frame(self._tk)
        self._btnSearch = Button(buttonFrame, text="Add")
        # binding call back command
        self._btnSearch.bind("<Button>", self.add_btn)
        self._btnModify = Button(buttonFrame, text="Search")
        # binding call back to search button
        self._btnModify.bind("<Button>", self.search_btn)
        self._btnList = Button(buttonFrame, text="List")
        # binding call back to list button
        self._btnList.bind("<Button>", self.list_btn)
        self._btnSearch.grid(row=0, column=1)
        self._btnModify.grid(row=0, column=2, padx=5)
        self._btnList.grid(row=0, column=3)

        scrollFrame = Frame(self._tk)
        self._sclText = ScrolledText(scrollFrame, width=30, height=5, wrap=WORD)
        self._sclText.grid(row=0, column=0)
        inputFrame.grid(row=0, column=0, pady=5)
        scrollFrame.grid(row=2, column=0, pady=5)
        buttonFrame.grid(row=1, column=0)

    def add_btn(self, event):
        try:
            email = self.lblEmail_var.get()
            name = self.lblName_var.get()
            rate = self.lblRate_var.get()
            instructor = Instructor(email, name, int(rate))
            # enable scroll_text first
            self._sclText.configure(state="normal")
            if email in self._instructors:
                self._sclText.insert(END, "Instructor already added!\n")
            else:
                self._instructors[email] = instructor
                self._sclText.insert(END, "Instructor added!\n")
            # scrolled to the latest line of text
            self._sclText.see(END)
            # disabled scroll text from meddling
            self._sclText.configure(state="disable")
        except TypeError:
            self._sclText.insert(
                END, "Please ensure no empty fields or invalid value is entered.\n"
            )
        except ValueError:
            self._sclText.insert(END, "Rate per day must be an integer.\n")

    def search_btn(self, event):
        try:
            email = self.lblEmail_var.get()
            # enable scrolled text
            self._sclText.configure(state="normal")
            if email not in self._instructors:
                self._sclText.insert(END, "No instructors with this email!\n")
            else:
                self._sclText.insert(END, f"{self._instructors[email]}")
            # scroll to latest line
            self._sclText.see(END)
            # disable scrolled text
            self._sclText.configure(state="disable")
        except TypeError:
            self._sclText.insert(END, "Please ensure Email is filled.\n")

    def list_btn(self, event):
        self._sclText.configure(state="normal")
        if not self._instructors:
            self._sclText.insert(END, "No instructors.\n")
        else:
            instructors = "\n".join(str(ins) for ins in self._instructors.values())
            self._sclText.insert(END, f"{instructors}")
        self._sclText.see(END)
        self._sclText.configure(state="disable")


if __name__ == "__main__":
    TrainingProviderGUI()
