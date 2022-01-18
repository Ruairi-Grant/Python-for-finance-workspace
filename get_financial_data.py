
from yahoofinancials import YahooFinancials
import pandas as pd
import os.path

# Transaction DataFrame Setup
if os.path.exists('user_stock_data.csv'):
    transaction_df = pd.read_csv('user_stock_data.csv')

else:
    transaction_columns = ['Date', 'Ticker', 'Type', 'Units',
                           'Price Per Unit', 'Total Price']
    transaction_df = pd.DataFrame(columns=transaction_columns)


user_input = input("1: Edit Transactions list\n"
                   "2: Stocks Eval\n"
                   "3: Portfolio Eval\n"
                   "Type \"Quit\" to quit\n"
                   ">>> ")


while (user_input != "Quit"):
    if (user_input == '4'):  # purly for testing
        print(transaction_df)
        user_input = input(">>> ")

    # TODO #2: output the current trading day data
    if (user_input == '2'):
        tickers = input(
            "Please enter your tickers seperated by a space: ").split()
        yf = YahooFinancials(tickers)
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
        print(df)

    # TODO #1:Allow user to enter past transactions and generate dataframes
    # loop that allows user to store all of their past trasactions
    if (user_input == '1'):
        while(user_input == '1'):  # TODO #5 add error checking
            trans_type = input("Enter transaction type. - Buy or Sell >>> ")
            ticker = input("Enter stock ticker\n>>> ")
            units = input("Enter number of units\n>>> ")
            ppu = input("Enter price per unit in USD\n>>> ")  # TODO #4
            date = input("Enter trans date in format DD-MM-YYYY\n>>> ")
            total_price = int(units)*int(ppu)
            transaction = {'Date': date, 'Ticker': ticker, 'Type': trans_type,
                           'Units': units, 'Price Per Unit': ppu,
                           'Total Price': total_price}
            print("Confirm Transaction: y/n\n", transaction, "\n")
            choice = input(">>>")
            if (choice == 'y'):  # add transaction to end of dataframe
                transaction_df = transaction_df.append(
                                                transaction, ignore_index=True)
                choice = input(
                    "Would you like to enter another transaction: y/n\n")
                if (choice == 'y'):  # add another transaction
                    user_input = '1'

                elif (choice == 'n'):  # leave the loop and print current data
                    user_input = '0'

            elif (choice == 'n'):  # user inputs details again
                user_input = '1'
        print(transaction_df)
        transaction_df.to_csv('user_stock_data.csv', index=False)

    # TODO #3:Output evaluation of overall portfolio
    if (user_input == '3'):
        print("Feature not ready yet\n")
    user_input = input(">>> ")
