import torch
import torch.nn as nn
import torch.optim as optim


# здесь объявляйте класс модели
class MyModel(nn.Module):
    def __init__(self, in_f=25, out_f=5):
        super().__init__()
        self.layer1 = nn.Linear(in_f, 16, bias=False)
        self.layer2 = nn.Linear(16, 8)
        self.out = nn.Linear(8, out_f, bias=False)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.tanh(x)
        x = self.layer2(x)
        x = torch.tanh(x)
        x = self.out(x)
        
        return x


x = torch.ones(48) # тензор в программе не менять

# здесь продолжайте программу
model = MyModel()
opt = optim.Adam(params=model.parameters(), lr=lr)
loss_func = nn.CrossEntropyLoss()

date_state_dict = {
    'loss': loss_func.state_dict(),
    'opt': opt.state_dict(),
    'model': model.state_dict()
}

torch.save(date_state_dict, "my_data_state.tar")
