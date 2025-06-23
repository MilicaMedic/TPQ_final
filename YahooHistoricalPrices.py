import yfinance as yf
import pandas as pd

# Tickers and date range
tickers = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'ADA-USD', 'DOGE-USD']
start_date = "2021-01-01"
end_date = "2025-03-31"

# Download data (MultiIndex: columns = (attribute, ticker))
df_raw = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False, progress = False)
print(df_raw)
# Stack to get long-form format
df_raw = df_raw.stack(level=1).reset_index()
df_raw.columns = ['date', 'tic', 'open', 'high', 'low', 'close', 'adj close', 'volume']

# Optional: drop adj_close if FinRL doesn't use it
df_finrl = df_raw[['date', 'tic', 'open', 'high', 'low', 'close', 'adj close', 'volume']]

# Preview
print(df_finrl.tail())

df_finrl.to_csv("data.csv", index=False)