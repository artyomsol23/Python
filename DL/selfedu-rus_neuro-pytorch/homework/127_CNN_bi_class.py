import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# здесь продолжайте программу
model = nn.Sequential(
    nn.Conv2d(1, 32, (5, 5), stride=1, padding=2, bias=True),
    nn.ReLU(inplace=True),
    nn.MaxPool2d((2, 2), stride=2),
    nn.Conv2d(32, 16, (3, 3), stride=1, padding=1, bias=True),
    nn.ReLU(inplace=True),
    nn.MaxPool2d((2, 2), stride=2),
    nn.Flatten(),
    nn.Linear(1024, 1)
)

d_train, d_test = data.random_split(ds, [0.7, 0.3])  # ds уже сформирован
train_data = data.DataLoader(d_train, batch_size=16, shuffle=True)
test_data = data.DataLoader(d_test, batch_size=len(d_test), shuffle=False)

optim = optim.Adam(params=model.parameters(), lr=0.01, weight_decay=0.01)
loss_func = nn.BCEWithLogitsLoss()

model.train()

epochs = 2

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y.unsqueeze(-1))

        optim.zero_grad()
        loss.backward()
        optim.step()

model.eval()

x_test, y_test = next(iter(test_data))

with torch.no_grad():
    predict = model(x_test)
    Q = torch.sum(predict.sign().flatten() == (2 * y_test.flatten() - 1)).item()

Q /= len(d_test)
