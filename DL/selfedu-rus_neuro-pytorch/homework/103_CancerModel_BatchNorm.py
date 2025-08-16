import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# здесь продолжайте программу
class CancerModel(nn.Module):
    def __init__(self, input_f=30, output_f=1):
        super().__init__()
        self.layer1 = nn.Linear(input_f, 32, bias=False)
        self.layer2 = nn.Linear(32, 20, bias=False)
        self.layer3 = nn.Linear(20, output_f)
        self.bm1 = nn.BatchNorm1d(32)
        self.bm2 = nn.BatchNorm1d(20)

    def forward(self, x):
        x = self.layer1(x)
        x = nn.functional.relu(x)
        x = self.bm1(x)
        x = self.layer2(x)
        x = nn.functional.relu(x)
        x = self.bm2(x)
        x = self.layer3(x)
        
        return x


model = CancerModel()

ds = data.TensorDataset(_global_var_data_x, _global_var_target.float())

d_train, d_test = data.random_split(ds, [0.7, 0.3])
train_data = data.DataLoader(d_train, batch_size=16, shuffle=True)
test_data = data.DataLoader(d_test, batch_size=len(d_test), shuffle=False)

optimizer = optim.Adam(params=model.parameters(), lr=0.01)
loss_func = nn.BCEWithLogitsLoss()

model.train()

epochs = 5

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y.unsqueeze(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

model.eval()

x_test, y_test = next(iter(test_data))

with torch.no_grad():
    p = model(x_test)
    
    Q = torch.sum(torch.sign(p.flatten()) == (2 * y_test.flatten() - 1)).item()

Q /= len(d_test)
