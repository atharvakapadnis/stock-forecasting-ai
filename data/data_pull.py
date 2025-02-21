import yfinance as yf
import pandas as pd

nvidia_stock = yf.download("NVDA", period="max", interval="1d")
nvidia_stock.reset_index(inplace=True)
nvidia_stock.to_csv("data/nvidia_stock.csv", index=False, header=True)
print("Data pulled and saved to data/nvidia_stock.csv")
