
class ProcessData:
    
    def __init__(self):
        pass

    def process_yfinance_data(self,data):
        # Reset the index
        data = data.reset_index()
        # Rename the columns
        for index, row in data.iterrows():
            result = []
            result.append({
                'date': row['Date'],
                'open': row['Open'],
                'high': row['High'],
                'low': row['Low'],
                'close': row['Close'],
                'volume': row['Volume']
            })
            return result
