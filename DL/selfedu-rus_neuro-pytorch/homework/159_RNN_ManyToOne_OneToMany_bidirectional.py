import torch
import torch.nn as nn


# здесь объявляйте класс модели
class BiRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn_1 = nn.RNN(
            input_size=5,
            hidden_size=9,
            num_layers=1,
            nonlinearity='tanh',
            bias=True, 
            batch_first=True,
            dropout=0.0,
            bidirectional=True
        )
        self.rnn_2 = nn.RNN(
            input_size=18,
            hidden_size=32,
            num_layers=1,
            nonlinearity='tanh',
            bias=True, 
            batch_first=True,
            dropout=0.0,
            bidirectional=False
        )
        self.output = nn.Linear(
            in_features=32,
            out_features=3,
            bias=True
        )
        self.out_length = 25

    def forward(self, x):
        _, h = self.rnn_1(x)
        y = torch.cat([h[0], h[1]], dim=1)     
        u = torch.zeros(y.size(0), self.out_length, y.size(1))
        u[:, 0, :] = y
        
        y, _ = self.rnn_2(u)
        n = y.size(1)
        out = torch.empty(y.size(0), n, self.output.out_features)

        for i in range(n):
            out[:, i, :] = self.output(y[:, i, :])
        
        return out

    
# тензор x в программе не менять
batch_size = 2
seq_length = 12
in_features = 5
x = torch.rand(batch_size, seq_length, in_features)

model = BiRNN()  # создание объекта модели

# здесь продолжайте программу
model.eval()

results = model(x)
