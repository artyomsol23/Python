import torch
import torch.nn as nn


# здесь продолжайте программу
class MyModel(nn.Module):
    def __init__(self, in_f, out_f):
        super().__init__()
        self.layer1 = nn.Linear(in_f, 32)
        self.layer2 = nn.Linear(32, 16)
        self.out = nn.Linear(16, out_f)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.relu(x)
        x = self.layer2(x)
        x = torch.relu(x)
        x = self.out(x)
        
        return x


model = MyModel(13, 3)
st = model.state_dict()
torch.save(st, 'func_nn.tar')
