import torch
import torch.nn as nn


# здесь объявляйте класс модели
class MyModel(nn.Module):
    def __init__(self, in_f=48, out_f=10):
        super().__init__()
        self.layer1 = nn.Linear(in_f, 32, bias=False)
        self.layer2 = nn.Linear(32, 16)
        self.out = nn.Linear(16, out_f)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.relu(x)
        x = self.layer2(x)
        x = torch.relu(x)
        x = self.out(x)
        
        return x


x = torch.ones(48) # тензор в программе не менять

# здесь продолжайте программу
model = MyModel()
st_model = torch.load('toy_nn.tar', weights_only=True)
model.load_state_dict(st_model)

predict = model(x)
