
from yahoofinancials import YahooFinancials
import pandas as pd



user_input = input(">>>")


while (user_input != "Quit"):
    if (user_input == 'Stocks Eval'):  #output the current trading day data #TODO #2 
        tickers = input("Please enter your tickers seperated by a space: ").split()
        yf = YahooFinancials(tickers)
        #set up names
        standard_data = ["regularMarketPrice", "regularMarketOpen", "regularMarketDayHigh", "regularMarketDayLow"]
        standard_data_names = ["Current Price", "Open", "Close", "Low"]
        #get data from Yahoo    
        curr_price = yf.get_stock_price_data()
        #turn dict into a nicly formatted DataFrame and print
        df = pd.DataFrame.from_dict(curr_price)
        df = df.transpose()
        df = df[standard_data]
        df.rename(columns = dict(zip(standard_data, standard_data_names)), inplace = True)
        print(df)

    if (user_input == 'Enter Transactions'): #Allow user to enter past transactions and generate relevant dataframes #TODO #1
        print("Feature not ready.\n")

    if (user_input == 'Portfolio Eval'): #Output evaluation of overall portfolio #TODO #3
        print("Feature not ready yet")

    user_input = input("Please choose and option:\n1:Current Price\n2:ratios and common indicators\n3:Plot of 5 year stock price\nType \"Quit\" to quit")