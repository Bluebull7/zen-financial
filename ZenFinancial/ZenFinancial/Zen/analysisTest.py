import unittest
import torch
from analysis import StockRNN

class TestStockRNN(unittest.TestCase):
    def setUp(self):
        self.input_size = 10
        self.hidden_size = 20
        self.num_layers = 2
        self.output_size = 1
        self.model = StockRNN(self.input_size, self.hidden_size, self.num_layers, self.output_size)

    def test_forward(self):
        batch_size = 3
        seq_length = 4
        input = torch.randn(batch_size, seq_length, self.input_size)
        output = self.model(input)
        self.assertEqual(output.size(), (batch_size, self.output_size))

    def test_model_parameters(self):
        self.assertEqual(self.model.hidden_size, self.hidden_size)
        self.assertEqual(self.model.num_layers, self.num_layers)
        self.assertIsInstance(self.model.lstm, nn.LSTM)
        self.assertIsInstance(self.model.fc, nn.Linear)

if __name__ == '__main__':
    unittest.main()