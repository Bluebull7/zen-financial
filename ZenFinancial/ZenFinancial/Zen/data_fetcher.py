import requests
import pandas as pd
import yfinance as yf
import processData


class DataFetcher:

    def __init__(self):
       self.process_yfinance_data = processData.ProcessData()

    def fetch_news(self, symbol):
        # Fetch news using the news API
        url = 'https://newsapi.org/v2/everything'
        params = {
            'q': symbol,
            }

        response = requests.get(url, params=params)
        data = response.json()
        articles = data['articles']
        news = pd.DataFrame(articles)
        return news
        
    def fetch_data(self, symbol, timeframe='daily', period='1y'):
        ticker = yf.Ticker(symbol)
        
        # Fetch historical data using yfinance
        data = ticker.history(period=period, interval=timeframe)
        
        # Convert to a format suitable for analysis
        data = processData.ProcessData(data)


        return data 

