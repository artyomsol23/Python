import torch
import torch.nn as nn


# здесь объявляйте класс LSTMToLinear
class LSTMToLinear(nn.Module):
    def forward(self, x):
        return x[1][0].squeeze(0)
    

# тензор x в программе не менять
batch_size = 18
seq_length = 21
in_features = 5
x = torch.rand(batch_size, seq_length, in_features)

# здесь продолжайте программу
model = nn.Sequential(
    nn.LSTM(
            input_size=in_features,
            hidden_size=25,
            num_layers=1,
            bias=True, 
            batch_first=True,
            dropout=0.0,
            bidirectional=False,
    ),
    LSTMToLinear(),
    nn.Linear(
        in_features=25,
        out_features=5,
        bias=True
    )
)

model.eval()

res = model(x)
