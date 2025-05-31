# TradeView Analytics

**TradeView Analytics** is a Python and Power BI-based tool for analyzing and visualizing stock market trends. 
It uses a historical stock dataset and generates insights through a Power BI dashboard.

## Features

- Processes stock data from a CSV file or Twelve Data API.
- Summarizes trends and patterns.
- Provides a Power BI dashboard for visualization.

## What is Twelve Data?

[Twelve Data](https://twelvedata.com/) is a financial market data platform that provides real-time and historical stock, forex, cryptocurrency, and ETF data via a developer-friendly API.

To fetch live stock data using the script, you'll need to sign up and get a free API key from Twelve Data.

# ⚙️ How It Works

## 1. Data Input

- Run the Python script `main.py`.
- The script prompts the user to **select one of the 30 predefined stocks**.
- Once selected, the script uses the **Twelve Data API** to fetch **real-time stock data for the past month**.
- The data is saved to `last_month_stock_data.csv`.

## 2. Data Processing

The script performs the following steps:

- Makes an API call to Twelve Data using the selected stock symbol.
- Cleans and structures the returned data.
- Saves the processed stock data to `last_month_stock_data.csv` for use in Power BI.

## 3. Output and Visualization

- Open `dashboard.pbix` in **Power BI Desktop**.
- Click **Refresh** under the *Home* tab to load the updated data.
- Use the **stock slicer** to select the stock you fetched via Python.
- The dashboard then shows the **latest one-month performance and analysis**.

> Stock logos are integrated from `stock_logos.csv` using Clearbit, providing visual context and company branding in the dashboard.


## Usage

1. Ensure you have Python 3.7+ installed.
2. Install required Python libraries (e.g., `pandas`, `requests`, `python-dotenv`).
3. Sign up at [twelvedata.com](https://twelvedata.com/) and obtain a free API key.
4. Create a `.env` file and add your API key like this:
   ```env
   TWELVEDATA_API_KEY=your_api_key_here
   
## Run the Python Script

```bash
python main.py
```
1. Select a stock when prompted.
2. The script will fetch the last 1 month of data and save it to last_month_stock_data.csv.

## Open the Dashboard in Power BI

1. Open dashboard.pbix in Power BI Desktop.
2. Click Refresh under the Home tab to load the updated data.
3. Use the stock slicer to select and explore the stock you fetched in Python.

## Directory Structure
```
TradeView Analytics/
├── main.py                      # Core data processing script
├── dashboard.pbix               # Power BI dashboard file
├── last_month_stock_data.csv    # Sample dataset
├── stock_logos.csv              # Stock list with associated Clearbit logo URLs
├── .gitignore                   # Git ignore rules
└── README.md                    # Project documentation
```
