
from yahoofinancials import YahooFinancials
import pandas as pd

#DataFrame Setup
transaction_columns = ['Date', 'Ticker', 'Type', 'Units', 'Price Per Unit', 'Total Price']
transaction_df = pd.DataFrame(columns= transaction_columns)

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
        while(user_input == 'Enter Transactions'):
            trans_type = input("Enter transaction type.\n>>> ")
            ticker = input("Enter stock ticker\n>>> ")
            units = input("Enter number of units\n>>> ")
            ppu = input("Enter price per unit in USD\n>>> ") #TODO #4
            date = input("Enter trans date in format DD-MM-YYYY\n>>> ")
            total_price = int(units)*int(ppu)
            transaction = {'Date':date, 'Ticker':ticker, 'Type':trans_type, 'Units':units, 'Price Per Unit':ppu, 'Total Price':total_price}
            print("Confirm Transaction: y/n\n",transaction,"\n")
            choice = input(">>>")
            if (choice == 'y'):
                transaction_df = transaction_df.append(transaction, ignore_index= True)
                choice = input("Would you like to enter another transaction: y/n\n")
                if (choice == 'y'):
                    user_input = 'Enter Transactions'
                
                elif (choice == 'n'):
                    user_input = '0'


            elif (choice == 'n'):
                user_input = 'Enter Transactions'

        print(transaction_df)
        


    if (user_input == 'Portfolio Eval'): #Output evaluation of overall portfolio #TODO #3
        print("Feature not ready yet\n")

    user_input = input(">>> ")