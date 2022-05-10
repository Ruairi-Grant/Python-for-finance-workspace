
from yahoofinancials import YahooFinancials
import pandas as pd
import matplotlib.pyplot as plt
import os.path

# Portfolio DataFrame setup
if os.path.exists('user_portfolio.csv'):
    portfolio_df = pd.read_csv('user_portfolio.csv')
else:
    portfolio_columns = ['Ticker', 'Quantity']
    portfolio_df = pd.DataFrame(columns=portfolio_columns)

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

# TODO #8
while (user_input != "Quit"):

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

    # TODO #1
    # allows user to enter past transactions and generate portfolio
    if (user_input == '1'):
        while(user_input == '1'):  # TODO #5 add error checking
            trans_type = input("Enter transaction type. - Buy or Sell >>> ")
            ticker = input("Enter stock ticker\n>>> ")
            units = int(input("Enter number of units\n>>> "))
            ppu = int(input("Enter price per unit in USD\n>>> "))  # TODO #4
            date = input("Enter trans date in format DD-MM-YYYY\n>>> ")
            total_price = units*ppu
            transaction = {'Date': date, 'Ticker': ticker, 'Type': trans_type,
                           'Units': units, 'Price Per Unit': ppu,
                           'Total Price': total_price}
            print("Confirm Transaction: y/n\n", transaction, "\n")
            choice = input(">>>")
            if (choice == 'y'):  # Add new data to Dataframes
                # add transaction to end of transaction_df and edit portfolio
                stock_idx = portfolio_df.index[
                                            portfolio_df['Ticker'] == ticker
                                            ].tolist()
                if not stock_idx:  # add new line to end of portfolio_df
                    portfolio_df = portfolio_df.append(
                                                {'Ticker': ticker,
                                                 'Quantity': units},
                                                ignore_index=True)
                else:  # edit the entry for this stock in the portfolio
                    if trans_type == 'Buy':  # user 'Bought' so add
                        portfolio_df.at[stock_idx[0], 'Quantity'] += int(units)
                    elif trans_type == 'Sell':  # user 'Sold' so subtract
                        portfolio_df.at[stock_idx[0], 'Quantity'] -= int(units)

                transaction_df = transaction_df.append(
                                                transaction, ignore_index=True)
                choice = input(
                    "Would you like to enter another transaction: y/n\n")
                if (choice == 'y'):  # add another transaction
                    user_input = '1'

                elif (choice == 'n'):  # leave the loop and print current data
                    user_input = '0'

            elif (choice == 'n'):  # return to top of editing
                user_input = '1'
        # Finished with editing: print data and save
        print("Transactions:")
        print(transaction_df)
        print("Portfolio:")
        print(portfolio_df)
        transaction_df.to_csv('user_stock_data.csv', index=False)
        portfolio_df.to_csv('user_portfolio.csv', index=False)

    # TODO #3:Output evaluation of overall portfolio
    if (user_input == '3'):
        # Output piechart of value for each stock
        tickers = portfolio_df['Ticker'].tolist()
        quantity_list = portfolio_df['Quantity'].tolist()

        yf = YahooFinancials(tickers)
        # set up names
        standard_data = ["regularMarketPrice"]
        standard_data_names = ["Current Price"]
        # get data from Yahoo
        curr_price = yf.get_stock_price_data()
        # turn dict into a nicly formatted DataFrame and print
        yf_data = pd.DataFrame.from_dict(curr_price)
        yf_data = yf_data.transpose()
        yf_data = yf_data[standard_data]
        yf_data.rename(
            columns=dict(zip(standard_data, standard_data_names)),
            inplace=True)
        yf_data = yf_data.reset_index(level=0).rename(columns={'index': 'Ticker'})
        portfolio_df = portfolio_df.join(yf_data["Current Price"])
        portfolio_df["Total Value"] = portfolio_df["Quantity"] * portfolio_df["Current Price"]
        fig1, ax1 = plt.subplots()
        ax1.pie(portfolio_df["Total Value"], labels=tickers, autopct='%1.1f%%',
                shadow=True, startangle=90)

        plt.show()
        print(portfolio_df)
        

    # Ask again for user input
    user_input = input("1: Edit Transactions list\n"
                       "2: Stocks Eval\n"
                       "3: Portfolio Eval\n"
                       "Type \"Quit\" to quit\n"
                       ">>> ")


"""
        fig1, ax1 = plt.subplots()
        ax1.pie(quantity_list, labels=tickers, autopct='%1.1f%%',
                shadow=True, startangle=90)

        plt.show()
"""