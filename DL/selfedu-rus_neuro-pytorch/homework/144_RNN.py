import torch
import torch.nn as nn


# здесь объявляйте класс модели
class MyRNN(nn.Module):
    def __init__(self, hidden_size=10):
        super().__init__()
        self.h_t = hidden_size
        self.inp = nn.Linear(16, self.h_t)
        self.out = nn.Linear(self.h_t, 5)

    def forward(self, x):
        batch_size = x.size(0)
        seq_length = x.size(1)
        h = torch.zeros(batch_size, self.h_t)

        for i in range(seq_length):
            a = self.inp(x[:, i, :])
            h = torch.tanh(a + h)

        y = self.out(h)
        y = torch.sigmoid(y)
        
        return y


batch_size = 8 # размер батча
seq_length = 6 # длина последовательности
in_features = 16 # размер каждого элемента последовательности
x = torch.rand(batch_size, seq_length, in_features)

# здесь объявляйте саму модель и продолжайте программу
model = MyRNN()

model.eval()

out = model(x)
