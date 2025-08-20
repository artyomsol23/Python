import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# здесь объявляйте класс модели
class AutoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(
                in_features=8,
                out_features=16,
                bias=True
            ),
            nn.ReLU(inplace=True),
            nn.Linear(
                in_features=16,
                out_features=4,
                bias=True
            ),
            nn.ReLU(inplace=True),
            nn.Linear(
                in_features=4,
                out_features=2,
                bias=True
            ),
            nn.Tanh(),
        )

        self.decoder = nn.Sequential(
            nn.Linear(
                in_features=2,
                out_features=4,
                bias=True
            ),
            nn.ReLU(inplace=True),
            nn.Linear(
                in_features=4,
                out_features=8,
                bias=True
            ),
        )

    def forward(self, x):
        h = self.encoder(x)
        return self.decoder(h), h


total = 1000 # размер выборки
data_x = torch.rand(total, 8) # обучающие данные

# здесь продолжайте программу
ds = data.TensorDataset(data_x, data_x)

train_data = data.DataLoader(ds, batch_size=16, shuffle=True)

model = AutoEncoder()

optim = optim.RMSprop(
    params=model.parameters(),
    lr=0.01,
    weight_decay=0.0001
)
loss_func = nn.MSELoss()

model.train()

epochs = 5

for _ in range(epochs):
    for x, y in train_data:
        predict, _ = model(x)
        loss = loss_func(predict, y)

        optim.zero_grad()
        loss.backward()
        optim.step()

model.eval()

predict, _ = model(data_x)

Q = loss_func(predict, data_x).item()
