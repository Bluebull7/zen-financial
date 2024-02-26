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

        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Load the data
data = pd.read_csv('data.csv')
data = data.dropna()
data = data[['Close']]
data = data.values
    
# Split the data into training and testing
train_data = data[:int(len(data)*0.8)]
test_data = data[int(len(data)*0.8):]

# Normalize the test_data   
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(-1, 1))
train_data_normalized = scaler.fit_transform(train_data)
test_data_normalized = scaler.fit_transform(test_data)

