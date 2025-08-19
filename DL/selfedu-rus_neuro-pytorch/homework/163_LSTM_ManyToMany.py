import torch
import torch.nn as nn


# здесь объявляйте класс OutputModule
class OutputModule(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(
            in_features=24,
            out_features=5,
            bias=True
        )

    def forward(self, x):
        batch_size = x[0].size(0)
        n = x[0].size(1)
        y = torch.empty(batch_size, n, self.layer.out_features)

        for i in range(n):
            y[:, i, :] = self.layer(x[0][:, i, :])
        
        return y


# тензор x в программе не менять
batch_size = 7
seq_length = 89
in_features = 3
x = torch.rand(batch_size, seq_length, in_features)

# здесь продолжайте программу
model = nn.Sequential(
    nn.LSTM(
            input_size=in_features,
            hidden_size=12,
            num_layers=1,
            bias=True, 
            batch_first=True,
            dropout=0.0,
            bidirectional=True
    ),
    OutputModule(),
)

model.eval()

out = model(x)
