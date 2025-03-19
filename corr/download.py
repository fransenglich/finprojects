from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import statsmodels as sm
import requests

def readKey() -> str:
    file = open("API-key.txt", "r")
    content = file.read()
    file.close()

    return content


api_key = readKey()


def get_listing_status(api_key):
    base_url = "https://www.alphavantage.co/query"
    function = "LISTING_STATUS"

    # Construct the API request URL
    api_url = f"{base_url}?function={function}&apikey={api_key}"

    # Send the API request and get the response
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        return None


def get_listing_status(api_key: str):
    csv_data = get_listing_status(api_key)

    f = open("listing_status.csv", "w")
    f.write(csv_data)
    f.close()


def download_ticker(ticker: str):
    ts = TimeSeries(api_key, output_format = 'pandas')

    data, meta_data = ts.get_monthly(ticker)
    data.to_csv("IBM5Y.csv")


def download_tickers(tickers):
    ts = TimeSeries(api_key, output_format = 'pandas')

    data: pd.DataFrame = None

    for t in tickers:
        data, meta_data = ts.get_daily(t, outputsize='full')

        #print(type(data))
        #print(data)

        data.to_csv(t + ".csv")

    # S&P 500 proxy, Fetch SPY, https://www.investopedia.com/markets/quote?tvwidgetsymbol=SPY


def main():
    #download_ticker('XLB')
    #download_tickers(['IBM', 'AAL', 'MMSI', 'NVDA', 'TIGO', 'SPY'])

    download_tickers(['XLB', 'XLC', 'XLE', 'XLF', 'XLI', 'XLK', 'XLP', 'XLU', 'XLV', 'XLY'])

main()
