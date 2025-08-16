import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# здесь продолжайте программу
class MyModel(nn.Module):
    def __init__(self, input_f=64, output_f=10):
        super().__init__()
        self.layer1 = nn.Linear(input_f, 64)
        self.layer2 = nn.Linear(64, 32)
        self.layer3 = nn.Linear(32, output_f)        
        self.dropout = nn.Dropout1d(0.3)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.relu(x)
        x = self.dropout(x)
        x = self.layer2(x)
        x = torch.relu(x)
        x = self.dropout(x)
        x = self.layer3(x)

        return x


model = MyModel()

ds = data.TensorDataset(_global_var_data_x, _global_var_target)

d_train, d_test = data.random_split(ds, [0.7, 0.3])
train_data = data.DataLoader(d_train, batch_size=16, shuffle=True)
test_data = data.DataLoader(d_test, batch_size=len(d_test), shuffle=False)    

optimizer = optim.Adam(params = model.parameters(), lr = 0.01, weight_decay=0.1)
loss_func = nn.CrossEntropyLoss()

model.train()

epochs = 2

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

model.eval()

with torch.no_grad():
    x_test, y_test = next(iter(test_data))
    predict = model(x_test) 
    predict = torch.argmax(predict, dim=1)

Q = (predict == y_test).float().mean().item()
