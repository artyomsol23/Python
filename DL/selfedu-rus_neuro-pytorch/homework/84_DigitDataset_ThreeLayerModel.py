import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# здесь продолжайте программу
class DigitDataset(data.Dataset):
    def __init__(self):
        self.data = _global_var_data_x
        self.target = _global_var_target
        self.length = len(self.data)

    def __getitem__(self, item):
        return self.data[item], self.target[item]

    def __len__(self):
        return self.length
        
class DigitClassModel(nn.Module):
    def __init__(self, in_f=64, out_f=10):
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
    
model = DigitClassModel()
model.train()

batch = 12
d_train = DigitDataset()
train_data = data.DataLoader(d_train, batch, shuffle=True)

optim = optim.Adam(params=model.parameters(), lr=0.01)
loss_func = torch.nn.CrossEntropyLoss()

epochs = 10

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y)
        
        optim.zero_grad()
        loss.backward()
        optim.step()

model.eval()
predict = model(d_train.data)
predict = torch.argmax(predict, dim=1)

Q = torch.mean((predict == d_train.target).float()).item()
