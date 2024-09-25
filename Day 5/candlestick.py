import yfinance as yf
import mplfinance as mpf

ticker = input("Enter the stock:  ")
df = yf.download(ticker, start="2023-08-01", end="2024-09-01")

mpf.plot(df, type='candle', style='charles', title=f'{ticker} Candlestick Chart', ylabel="Price")