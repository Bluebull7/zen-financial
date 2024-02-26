import requests
import pandas as pd

class Data_Fetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, symbol, function, outputsize):
        url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&outputsize={outputsize}&apikey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.columns = pd.to_datetime(df.columns)
        df.sort_index(inplace=True)
        return df