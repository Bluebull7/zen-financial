import pandas as pd 
import numpy as np 
import torch
import torch.nn as nn

class StockRNN(nn.module):
    #RNN Model definition using PyTorch

    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(StockRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(device)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') 

# Split the data into training and testing
train_data = data[:int(len(data)*0.8)]
test_data = data[int(len(data)*0.8):]

# Normalize the test_data   
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data)
test_data_normalized = scaler.fit_transform(test_data)

def load_data(symbol):
    # Fetch data using the Yahoo Finance API 
    data = yf.download(symbol, start="2017-01-01", end="2021-01-01")
    data = data.dropna()
    data = data[['Close']]
    return data

def train_model(train_data, input_size, hidden_size, num_layers, output_size, num_epochs):
    # Train the model using the training data
    model = StockRNN(input_size, hidden_size, num_layers, output_size).to(device)
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    train_data_normalized = torch.FloatTensor(train_data_normalized).view(-1)
    train_data_normalized = train_data_normalized.to(device)
    train_data_normalized = train_data_normalized.view(1, -1)
    for epoch in range(num_epochs):
        outputs = model(train_data_normalized)
        optimizer.zero_grad()
        loss = criterion(outputs, train_data_normalized)
        loss.backward()
        optimizer.step()
        if epoch % 100 == 0:
            print(f'Epoch {epoch} Loss {loss.item()}')
    return model


def test_model(model, test_data):
    # Test the model using the testing data
    test_data_normalized = torch.FloatTensor(test_data_normalized).view(-1)
    test_data_normalized = test_data_normalized.to(device)
    test_data_normalized = test_data_normalized.view(1, -1)
    outputs = model(test_data_normalized)
    return outputs

def main():
    symbol = 'AAPL'
    data = load_data(symbol)
    input_size = 1
    hidden_size = 64
    num_layers = 1
    output_size = 1
    num_epochs = 1000
    model = train_model(train_data, input_size, hidden_size, num_layers, output_size, num_epochs)
    predictions = test_model(model, test_data)
    print(predictions)

if __name__ == "__main__":
    main()

