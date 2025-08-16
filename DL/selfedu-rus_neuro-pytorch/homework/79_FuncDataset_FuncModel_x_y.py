import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


class FuncDataset(data.Dataset):
    def __init__(self):
        _range = torch.arange(-3, 3, 0.1)
        self.data = torch.tensor([(_x, _y) for _x in _range for _y in _range])
        self.target = self._func(self.data)
        self.length = len(self.data) # размер обучающей выборки

    @staticmethod
    def _func(coord):
        _x, _y = coord[:, 0], coord[:, 1]
        return torch.sin(2 * _x) * torch.cos(3 * _y) + 0.2 * torch.cos(10 * _x) * torch.sin(8 * _x) + 0.1 * _x ** 2 + 0.1 * _y ** 2

    def __getitem__(self, item):
        # возврат образа по индексу item в виде кортежа: (данные, целевое значение)
        return self.data[item], self.target[item]
        
    def __len__(self):
        # возврат размера выборки
        return self.length
        

class FuncModel(nn.Module):
    def __init__(self):
        super().__init__()
        # модель однослойной полносвязной нейронной сети:
        # 1-й слой: число входов 6 (x, x^2, x^3, y, y^2, y^3), число нейронов 1
        self.layer1 = nn.Linear(6, 1)

    def forward(self, coord):
        x, y = coord[:, 0], coord[:, 1]
        x.unsqueeze_(-1)
        y.unsqueeze_(-1)

        xx = torch.empty(coord.size(0), 6)
        xx[:, :3] = torch.cat([x, x ** 2, x ** 3], dim=1)
        xx[:, 3:] = torch.cat([y, y ** 2, y ** 3], dim=1)
        y = self.layer1(xx)
        
        return y


# здесь продолжайте программу
batch_size = 16
epochs = 20

d_train = FuncDataset()
train_data = data.DataLoader(d_train, batch_size, shuffle=True)

model = FuncModel()
model.train

optim = optim.RMSprop(params=model.parameters(), lr=0.01)
loss_func = torch.nn.MSELoss()

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y.unsqueeze(-1))
        
        optim.zero_grad()
        loss.backward()
        optim.step()
        
model.eval()
predict = model(d_train.data)

Q = loss_func(predict, d_train.target.unsqueeze(-1)).item()
