

from yahoofinancials import YahooFinancials
import pandas as pd

ticker = 'AAPL'
yf = YahooFinancials(ticker)

income_statement = yf.get_financial_stmts('annual', 'income')
aapl_is = income_statement['incomeStatementHistory']['AAPL']

df_list = []

for d in aapl_is:
    df_list.append(pd.DataFrame.from_dict(d, orient='index'))
    
df_is = pd.concat(df_list)

print(df_is)