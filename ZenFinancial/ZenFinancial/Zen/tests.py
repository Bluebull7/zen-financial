import django

from django.test import TestCase

# Create your tests here.
import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from data_fetcher import DataFetcher


class TestDataFetcher(unittest.TestCase):
    @patch("yfinance.Ticker")
    def test_fetch_data(self, mock_ticker):
        # Mock the yfinance Ticker and its history method
        mock_data = pd.DataFrame(
            {
                "Open": [1, 2, 3],
                "High": [1, 2, 3],
                "Low": [1, 2, 3],
                "Close": [1, 2, 3],
                "Volume": [1, 2, 3],
            }
        )
        mock_ticker.return_value.history.return_value = mock_data

        # Initialize DataFetcher and call fetch_data
        fetcher = DataFetcher()
        result = fetcher.fetch_data("AAPL")

        # Assert that the Ticker was called with the correct symbol
        mock_ticker.assert_called_once_with("AAPL")

        # Assert that the history method was called with the correct parameters
        mock_ticker.return_value.history.assert_called_once_with(
            period="1y", interval="daily"
        )

        # Assert that the result is as expected
        expected_result = [
            {
                "date": pd.Timestamp("1970-01-01 00:00:00"),
                "open": 1,
                "high": 1,
                "low": 1,
                "close": 1,
                "volume": 1,
            },
            {
                "date": pd.Timestamp("1970-01-01 00:00:00"),
                "open": 2,
                "high": 2,
                "low": 2,
                "close": 2,
                "volume": 2,
            },
            {
                "date": pd.Timestamp("1970-01-01 00:00:00"),
                "open": 3,
                "high": 3,
                "low": 3,
                "close": 3,
                "volume": 3,
            },
        ]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
