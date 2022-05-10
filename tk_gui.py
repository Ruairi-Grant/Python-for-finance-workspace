"""
Tutorial for tkinter: https://tkdocs.com/tutorial/firstexample.html
"""
from tkinter import *
from tkinter import ttk


class PortfolioGUI:

    def __init__(self, root):

        root.title("Main Menu")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Stock Analysis", command=self.stockEval).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="Edit Transactions", command=self.editTrans).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text="Portfolio Analysis", command=self.portfolioEval).grid(column=3, row=3, sticky=W)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass

    def stockEval(self):
        t = Toplevel()
        t.title("Stock Evaluation")

    def editTrans(self):
        t = Toplevel()
        t.title("Edit Transactions")

    def portfolioEval(self):
        t = Toplevel()
        t.title("Portfolio Evaluation")


root = Tk()
PortfolioGUI(root)
root.mainloop()
