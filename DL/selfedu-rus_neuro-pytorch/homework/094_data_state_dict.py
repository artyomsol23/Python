import torch
import torch.nn as nn
import torch.optim as optim


# здесь объявляйте класс модели
class MyModel(nn.Module):
    def __init__(self, in_f=10, out_f=6):
        super().__init__()
        self.layer1 = nn.Linear(in_f, 8)
        self.layer2 = nn.Linear(8, 4)
        self.out = nn.Linear(4, out_f)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.sigmoid(x)
        x = self.layer2(x)
        x = torch.sigmoid(x)
        x = self.out(x)
        
        return x


x = torch.ones(48) # тензор в программе не менять

# здесь продолжайте программу
model = MyModel()
opt = optim.RMSprop(params=model.parameters(), lr=0.05)
st = torch.load('nn_data_state.tar', weights_only=True)

model.load_state_dict(st['model'])
opt.load_state_dict(st['opt'])
