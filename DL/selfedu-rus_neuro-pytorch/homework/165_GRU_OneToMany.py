import torch
import torch.nn as nn


# здесь объявляйте класс модели
class GRURNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.gru = nn.GRU(
            input_size=2,
            hidden_size=5,
            num_layers=1,
            bias=False,
            batch_first=True,
            dropout=0,
            bidirectional=True
        )
        self.mb = nn.BatchNorm1d(10)
        self.output = nn.Linear(
            in_features=10,
            out_features=4,
            bias=True
        )

    def forward(self, x):
        y, _ = self.gru(x)
        n = y.size(1)
        out = torch.empty(y.size(0), n, self.output.out_features)

        for i in range(n):
            out[:, i, :] = self.output(self.mb(y[:, i, :]))
        
        return out


# тензор x в программе не менять
batch_size = 3
seq_length = 17
d_size = 2
x = torch.rand(batch_size, d_size)

# здесь продолжайте программу
model = GRURNN() # здесь создавайте объект модели

model.eval()

u = torch.zeros(batch_size, seq_length, d_size)
u[:, 0, :] = x

predict = model(u)
