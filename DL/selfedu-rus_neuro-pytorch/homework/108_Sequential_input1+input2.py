import torch
import torch.nn as nn


# здесь объявляйте класс модели
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.inp_2 = nn.Sequential(
            nn.Linear(12, 12, bias=True),
            nn.Sigmoid()
        )
        self.out = nn.Sequential(
            nn.Linear(12, 32, bias=True),
            nn.ReLU(),
            nn.Linear(32, 1, bias=True)
        )
        self.inp_1 = nn.Sequential(
            nn.Linear(7, 12, bias=True),
            nn.Tanh()
        )

    def forward(self, a, b):
        x1, x2 = self.inp_1(a), self.inp_2(b)
        return self.out(x1 + x2)
    

batch_size = 12
a = torch.rand(batch_size, 7)  # тензоры a, b в программе не менять
b = torch.rand(batch_size, 12)

# здесь продолжайте программу
model = MyModel()

model.eval()

predict = model(a, b)
