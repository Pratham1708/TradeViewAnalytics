import os
from dotenv import load_dotenv
import requests
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Get API key from environment
API_KEY = os.getenv('TWELVEDATA_API_KEY')

# Sample stock symbols
sample_symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
                  "NVDA", "META", "NFLX", "INTC", "ADBE",
                  "ORCL", "IBM", "AMD", "BA", "BABA",
                  "DIS", "PEP", "KO", "NKE", "PYPL"]

# Display stock options
print("Available stock symbols:")
for idx, sym in enumerate(sample_symbols, 1):
    print(f"{idx}. {sym}")

symbol = input("\nEnter one of the above stock symbols: ").strip().upper()

if symbol not in sample_symbols:
    print("❌ Invalid symbol. Please run again.")
else:
    url = f"https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&outputsize=30&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if "values" not in data:
        print("❌ Error:", data.get("message", "Unknown error"))
    else:
        df = pd.DataFrame(data["values"])
        df['symbol'] = symbol
        df.rename(columns={"datetime": "Date"}, inplace=True)
        df = df[['Date', 'symbol', 'open', 'high', 'low', 'close', 'volume']]
        df.sort_values(by='Date', inplace=True)
        df.to_csv("last_month_stock_data.csv", index=False)
        print(f"✅ Data saved to last_month_stock_data.csv")
