
from yahoofinancials import YahooFinancials
import pandas as pd


tickers = input("Please enter your tickers seperated by a space: ").split()
user_input = input("Please choose an option:\n1:Current Price\n2:Ratios and Common Indicators\n3:Plot of 5 year stock price\nType \"Quit\" to quit\n")

yf = YahooFinancials(tickers)

while (user_input != "Quit"):
  if (user_input == '1'):  #output the current trading day data
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

  if (user_input == '2'): #utput a tabel of common stock indicators
    standard_data = ["regularMarketPrice", "regularMarketOpen", "regularMarketDayHigh", "regularMarketDayLow"]


  user_input = input("Please choose and option:\n1:Current Price\n2:ratios and common indicators\n3:Plot of 5 year stock price\nType \"Quit\" to quit")