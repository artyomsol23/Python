import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензора x)
class ThreeLayersModel(nn.Module):
    def __init__(self, n_input, hidden1, hidden2, n_output):
        super().__init__()
        self.layer1 = nn.Linear(n_input, hidden1)
        self.layer2 = nn.Linear(hidden1, hidden2)
        self.layer3 = nn.Linear(hidden2, n_output)
        
    def forward(self, x):
        x = self.layer1(x)
        x = torch.tanh(x)
        x = self.layer2(x)
        x = torch.tanh(x)
        x = self.layer3(x)
        x = torch.tanh(x)

        return x


batch_size = 4
x = torch.rand(batch_size, 32) # тензор x в программе не менять

# здесь продолжайте программу
model = ThreeLayersModel(32, 10, 12, 1)
model.eval()

predict = model(x)
