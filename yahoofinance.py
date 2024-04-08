import yfinance as yf
import pandas as pd

msft = yf.Ticker('MSFT')

# Balance Sheet
df = pd.DataFrame(msft.balance_sheet / 1000000)
df.to_csv('MSFTBalanceSheet.csv')

# Income Statement
df = pd.DataFrame(msft.income_stmt / 1000000)
df.to_csv('MSFTIncomeStatement.csv')

# Cash Flow
df = pd.DataFrame(msft.cash_flow / 1000000)
df.to_csv('MSFTCashFlow.csv')


