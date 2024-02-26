import requests
import pandas as pd

class Data_Fetcher:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_data(self, symbol, function, outputsize):
        base_url = "https://www.alphavantage.co/query"
        datatype = "json"

        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
            "datatype": datatype,
            "outputsize": outputsize
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # Parse the result into a pandas DataFrame
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df = df.apply(pd.to_numeric)

        # Convert the index to datetime format
        df.index = pd.to_datetime(df.index)

        return df