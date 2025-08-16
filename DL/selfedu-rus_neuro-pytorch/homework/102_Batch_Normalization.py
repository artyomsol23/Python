import torch
import torch.nn as nn


# здесь объявляйте класс модели (важно именно здесь)
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(10, 64, bias=False)
        self.layer2 = nn.Linear(64, 1)
        self.bm1 = nn.BatchNorm1d(64)
        self.act = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.layer1(x)
        x = self.act(x)
        x = self.bm1(x)
        x = self.layer2(x)
        
        return x


model = MyModel()  # здесь создавайте объект модели

batch_size = 16
x = torch.rand(batch_size, 10)  # этот тензор в программе не менять

# здесь продолжайте программу
model.eval()

predict = model(x)
