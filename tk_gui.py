"""
Tutorial for tkinter: https://tkdocs.com/tutorial/firstexample.html
"""
from tkinter import *
from tkinter import ttk
from pandastable import Table

from yahoofinancials import YahooFinancials
import pandas as pd
import matplotlib.pyplot as plt
import os.path


class StockEval:

    def __init__(self):
        t = Toplevel()
        t.title("Stock Evaluation")

        self.stockEvalFrame = ttk.Frame(t, padding="3 3 12 12")
        self.stockEvalFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        self.tickers = StringVar()
        ticker_entry = ttk.Entry(self.stockEvalFrame, width=7, textvariable=self.tickers)
        ticker_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.stockEvalFrame, text="Enter stock ticker for evaluation:").grid(column=1, row=1, sticky=W)

        ttk.Button(self.stockEvalFrame, text="Stock Analysis", command=self.getStockData).grid(column=2, row=2, sticky=W)

    def getStockData(self, *args):
        tickersList = ((self.tickers).get()).split()
        yf = YahooFinancials(tickersList)
        # set up names
        standard_data = ["regularMarketPrice", "regularMarketOpen",
                         "regularMarketDayHigh", "regularMarketDayLow"]
        standard_data_names = ["Current Price", "Open", "Close", "Low"]
        # get data from Yahoo
        curr_price = yf.get_stock_price_data()
        # turn dict into a nicly formatted DataFrame and print
        df = pd.DataFrame.from_dict(curr_price)
        df = df.transpose()
        df = df[standard_data]
        df.rename(
            columns=dict(zip(standard_data, standard_data_names)),
            inplace=True)

        pt = Table(self.stockEvalFrame, dataframe=df,
                   showtoolbar=True, showstatusbar=True)

        pt.showIndex()
        pt.show()


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

        ttk.Label(portfolioEvalFrame, text="Enter Transaction type:").grid(column=1, row=1, sticky=W)


class EditTransaction:

    def __init__(self):
        t = Toplevel()
        t.title("Edit transactions")

        self.transactionEditFrame = ttk.Frame(t, padding="3 3 12 12")
        self.transactionEditFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        t.columnconfigure(0, weight=1)
        t.rowconfigure(0, weight=1)

        ttk.Label(self.transactionEditFrame, text="Enter Transaction type:").grid(column=1, row=1, sticky=W)
        self.transType = StringVar()
        typeEntry = OptionMenu(self.transactionEditFrame, self.transType, "Buy", "Sell")
        typeEntry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.transactionEditFrame, text="Enter Transaction ticker:").grid(column=1, row=2, sticky=W)
        self.transTicker = StringVar()
        typeEntry = ttk.Entry(self.transactionEditFrame, width=7, textvariable=self.transTicker)
        typeEntry.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.transactionEditFrame, text="Enter Number of units:").grid(column=1, row=3, sticky=W)
        self.transUnits = StringVar()
        typeEntry = ttk.Entry(self.transactionEditFrame, width=7, textvariable=self.transUnits)
        typeEntry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.transactionEditFrame, text="Enter the price per unit:").grid(column=1, row=4, sticky=W)
        self.transPrice = StringVar()
        typeEntry = ttk.Entry(self.transactionEditFrame, width=7, textvariable=self.transPrice)
        typeEntry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(self.transactionEditFrame, text="Enter the data of the transaction:").grid(column=1, row=5, sticky=W)
        self.transDate = StringVar()
        typeEntry = ttk.Entry(self.transactionEditFrame, width=7, textvariable=self.transDate)
        typeEntry.grid(column=2, row=5, sticky=(W, E))

        ttk.Button(self.transactionEditFrame, text="Enter transaction", command=self.enterTransaction).grid(column=2, row=6, sticky=W)

    def enterTransaction(self, *args):
        print(self.transType, self.transTicker, self.transUnits, self.transPrice, self.transDate)

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
