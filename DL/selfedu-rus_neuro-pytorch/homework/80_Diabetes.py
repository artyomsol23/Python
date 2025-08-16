import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# здесь продолжайте программу
class MyDataset(data.Dataset):
    def __init__(self):
        self.data = _global_var_data_x
        self.target = _global_var_target.unsqueeze(1)
        self.length = len(self.data) # self.data.size(0)

    def __getitem__(self, indx):
        return self.data[indx], self.target[indx]
        
    def __len__(self):
        return self.length
        

class MyModel(nn.Module):
    def __init__(self, f_input=10, hidden=64, f_output=1):
        super().__init__()
        self.layer1 = nn.Linear(f_input, hidden)
        self.out = nn.Linear(hidden, f_output)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.tanh(x)
        x = self.out(x)
        
        return x


batch = 8
d_train = MyDataset()
train_data = data.DataLoader(d_train, batch, shuffle=True)

model = MyModel()
model.train

optim = optim.RMSprop(params=model.parameters(), lr=0.01)
loss_func = torch.nn.MSELoss()

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

Q = loss_func(predict, d_train.target).item()
