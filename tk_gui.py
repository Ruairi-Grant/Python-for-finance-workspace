"""
Tutorial for tkinter: https://tkdocs.com/tutorial/firstexample.html
"""
from tkinter import *
from tkinter import ttk


class StockEval:

    def __init__(self):
        t = Toplevel()
        t.title("Stock Evaluation")

        stockEvalFrame = ttk.Frame(t, padding="3 3 12 12")
        stockEvalFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        ticker = StringVar()
        ticker_entry = ttk.Entry(stockEvalFrame, width=7, textvariable=ticker)
        ticker_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(stockEvalFrame, text="feet").grid(column=3, row=1, sticky=W)


class PortfolioEval:

    def __init__(self):
        t = Toplevel()
        t.title("Portfolio Evaluation")

        portfolioEvalFrame = ttk.Frame(t, padding="3 3 12 12")
        portfolioEvalFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        ticker = StringVar()
        ticker_entry = ttk.Entry(portfolioEvalFrame, width=7, textvariable=ticker)
        ticker_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(portfolioEvalFrame, text="XXX").grid(column=3, row=1, sticky=W)


class EditTransaction:

    def __init__(self):
        t = Toplevel()
        t.title("Edit transactions")

        transactionEditFrame = ttk.Frame(t, padding="3 3 12 12")
        transactionEditFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        ticker = StringVar()
        ticker_entry = ttk.Entry(transactionEditFrame, width=7, textvariable=ticker)
        ticker_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(transactionEditFrame, text="YYY").grid(column=3, row=1, sticky=W)


class PortfolioGUI:

    def __init__(self, root):

        root.title("Main Menu")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Stock Analysis", command=StockEval).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text="Edit Transactions", command=EditTransaction).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text="Portfolio Analysis", command=PortfolioEval).grid(column=3, row=3, sticky=W)


root = Tk()
PortfolioGUI(root)
root.mainloop()
