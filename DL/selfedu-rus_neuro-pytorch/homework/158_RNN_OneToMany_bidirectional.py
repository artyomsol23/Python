import torch
import torch.nn as nn


# здесь объявляйте класс модели
class OneToManyRNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.rnn_1 = nn.RNN(
            input_size=5,
            hidden_size=7,
            num_layers=1,
            nonlinearity='tanh',
            bias=True, 
            batch_first=True,
            dropout=0,
            bidirectional=True
        )
        self.output = nn.Linear(
            in_features=14,
            out_features=2,
            bias=True
        )

    def forward(self, x):
        y, h = self.rnn_1(x)
        n = y.size(1)
        out = torch.empty(y.size(0), n, self.output.out_features)

        for i in range(n):
            out[:, i, :] = self.output(y[:, i, :])
            
        return out


# тензор x в программе не менять
batch_size = 4
seq_length = 12
d_size = 5
x = torch.rand(batch_size, d_size)

model = OneToManyRNN()

# здесь продолжайте программу
model.eval()

u = torch.zeros(batch_size, seq_length, d_size) # не забудь про нули
u[:, 0, :] = x

predict = model(u)
