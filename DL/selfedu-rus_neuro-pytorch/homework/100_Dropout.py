import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензора x)
class MyModel(nn.Module):
    def __init__(self, input_f=13, output_f=3):
        super().__init__()
        self.layer1 = nn.Linear(input_f, 32)
        self.layer2 = nn.Linear(32, 16)
        self.layer3 = nn.Linear(16, output_f)
        self.dropout1 = nn.Dropout(0.4)

    def forward(self, x):
        x = self.layer1(x)
        x = nn.functional.relu(x)
        x = self.layer2(x)
        x = nn.functional.relu(x)
        x = self.dropout1(x)
        x = self.layer3(x)
      
        return x


model = MyModel() # здесь создавайте объект модели

x = torch.rand(13)

# здесь продолжайте программу для вычисления predict
model.eval()
x = torch.rand(13)

predict = model(x.unsqueeze(0)) # двумерный тензор (батч примеров)
