import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензора x)
class TwoLayerModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(3, 2)
        self.out = nn.Linear(2, 1)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.sigmoid(x)
        x = self.out(x)
        
        return x


x = torch.rand(3) # тензор x в программе не менять

# здесь продолжайте программу
model = TwoLayerModel()
model.eval()

predict = model(x)
