import torch
import torch.nn as nn


# здесь объявляйте класс модели
class ManyToOneRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn = nn.RNN(
            input_size=32,
            hidden_size=12,
            num_layers=1,
            nonlinearity='tanh',
            bias=True, 
            batch_first=True,
            dropout=0.0,
            bidirectional=True,
        )
        self.out = nn.Linear(
            in_features=24,
            out_features=5,
            bias=True
        )

    def forward(self, x):
        _, h = self.rnn(x)
        y = torch.cat([h[0], h[1]], dim=1)
        
        return self.out(y)


batch_size = 8
seq_length = 12
d_size = 32

x = torch.rand(batch_size, seq_length, d_size)

model = ManyToOneRNN() # создание объекта модели

# здесь продолжайте программу
model.eval()

predict = model(x)
