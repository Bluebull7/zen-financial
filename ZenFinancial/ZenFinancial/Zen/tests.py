from django.test import TestCase

# Create your tests here.
import unittest
from unittest.mock import patch
import pandas as pd
from data_fetcher import Data_Fetcher

class TestDataFetcher(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data(self, mock_get):
        # Mock the JSON response from Alpha Vantage
        mock_response = {
            'Time Series (Daily)': {
                '2022-01-01': {'1. open': '100.0', '2. high': '101.0', '3. low': '99.0', '4. close': '100.5', '5. volume': '1000000'},
                '2022-01-02': {'1. open': '101.0', '2. high': '102.0', '3. low': '100.0', '4. close': '101.5', '5. volume': '1000000'}
            }
        }
        mock_get.return_value.json.return_value = mock_response
        
    
        fetcher = Data_Fetcher('dummy_api_key')
        df = fetcher.fetch_data('MSFT', 'TIME_SERIES_DAILY', 'compact')
        
        # change the columns to datetime format
        df.columns = pd.to_datetime(df.columns)
        
        # Check that the DataFrame has the corrcect shape
        self.assertEqual(df.shape, (2, 5))

        # Check that the DataFrame has the correct column names
        expected_columns = pd.to_datetime(['2022-01-01', '2022-01-02'])
        pd.testing.assert_index_equal(df.columns, expected_columns)

if __name__ == '__main__':
    unittest.main()