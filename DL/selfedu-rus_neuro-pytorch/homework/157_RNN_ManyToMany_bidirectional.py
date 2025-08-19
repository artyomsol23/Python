import torch
import torch.nn as nn


# здесь объявляйте класс OutputModule
class OutputModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(
            in_features=8,
            out_features=2,
            bias=False
        )

    def forward(self, x):
        batch_size = x[0].size(0)
        n = x[0].size(1)
        y = torch.empty(batch_size, n, self.layer.out_features)

        for i in range(n):
            y[:, i, :] = self.layer(x[0][:, i, :])
        
        return y


# тензор x в программе не менять
batch_size = 4
seq_length = 64
in_features = 5
x = torch.rand(batch_size, seq_length, in_features)

# создание объекта модели
model = nn.Sequential(
    nn.RNN(
        input_size=in_features,
        hidden_size=4,
        num_layers=1,
        nonlinearity='tanh',
        bias=True, 
        batch_first=True,
        dropout=0,
        bidirectional=True
    ),
    OutputModule()
)

# здесь продолжайте программу
model.eval()

out = model(x)
    
