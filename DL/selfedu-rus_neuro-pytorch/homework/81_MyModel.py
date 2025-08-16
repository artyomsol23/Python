import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# здесь продолжайте программу
class MyDataset(data.Dataset):
    def __init__(self):
        _x = torch.arange(-6, 6, 0.1)
        self.data = _x
        self.target = 0.5 * _x + torch.sin(2 * _x) - 0.1 * torch.exp(_x / 2) - 12.5
        self.length = len(self.data)

    def __getitem__(self, indx):
        return self.data[indx], self.target[indx]
        
    def __len__(self):
        return self.length
        

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(3, 1)

    def forward(self, x):
        # исходный тензор (batch_size,)
        x.unsqueeze_(-1)  # inplace_
        # для дальнейших операций нужно (batch_size, 1)
        xx = torch.cat([x, x ** 2, x ** 3], dim=1)
        y = self.layer1(xx)
        
        return y


batch = 10
d_train = MyDataset()
train_data = data.DataLoader(d_train, batch, shuffle=True)

model = MyModel()
model.train

optim = optim.RMSprop(params=model.parameters(), lr=0.1)
loss_func = torch.nn.MSELoss()

epochs = 20

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y.unsqueeze(-1))  # predict и y должны иметь одинаковую форму
        
        optim.zero_grad()
        loss.backward()
        optim.step()
        
model.eval()
predict = model(d_train.data)

Q = loss_func(predict, d_train.target.unsqueeze(-1)).item()
