# import libraries
import yfinance as yf
import pandas as pd

# download data
df = yf.download(
    "^GSPC",       # S&P 500
    start = "1995-01-01", # from Jan 1995
    end = "2024-12-31"    # to Dec 2024
)

if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.droplevel(1)

# save data
df.to_csv("data/sp500.csv")