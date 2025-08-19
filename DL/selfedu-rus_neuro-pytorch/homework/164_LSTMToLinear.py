import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# здесь объявляйте класс LSTMToLinear
class LSTMToLinear(nn.Module):
    def forward(self, x):
        return x[1][0].squeeze(0)


# здесь описывайте модель с помощью класса Sequential
model = nn.Sequential(
    nn.LSTM(
        input_size=1,
        hidden_size=10,
        num_layers=1,
        bias=True, 
        batch_first=True,
        dropout=0.0,
        bidirectional=False
    ),
    LSTMToLinear(),
    nn.Linear(
        in_features=10,
        out_features=1,
        bias=True
    )
)

x = torch.linspace(-10, 10, 2000)
y = torch.cos(x) + 0.5 * torch.sin(5*x) + 0.1 * torch.randn_like(x) + 0.2 * x

total = len(x)      # общее количество отсчетов
train_size = 1000   # размер обучающей выборки
seq_length = 20     # число предыдущих отсчетов, по которым строится прогноз следующего значения

y.unsqueeze_(1)
train_data_y = torch.cat([y[i:i+seq_length] for i in range(train_size-seq_length)], dim=1)
train_targets = torch.tensor([y[i+seq_length].item() for i in range(train_size-seq_length)])

test_data_y = torch.cat([y[i:i+seq_length] for i in range(train_size-seq_length, total-seq_length)], dim=1)
test_targets = torch.tensor([y[i+seq_length].item() for i in range(train_size-seq_length, total-seq_length)])

d_train = data.TensorDataset(train_data_y.permute(1, 0), train_targets)
d_test = data.TensorDataset(test_data_y.permute(1, 0), test_targets)

train_data = data.DataLoader(d_train, batch_size=8, shuffle=True)
test_data = data.DataLoader(d_test, batch_size=len(d_test), shuffle=False)

# оптимизатор RMSprop с шагом обучения 0.01
optim = optim.RMSprop(params=model.parameters(), lr=0.01)
# функция потерь - средний квадрат ошибок
loss_func = nn.MSELoss()

# переведите модель в режим обучения
model.train()

epochs = 5 # число эпох

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x.unsqueeze(-1)).squeeze() # вычислите прогноз модели для x_train
        loss = loss_func(predict, y) # вычислите потери для predict и y_train

        # выполните один шаг обучения (градиентного спуска)
        optim.zero_grad()
        loss.backward()
        optim.step()

# переведите модель в режим эксплуатации
model.eval()

d, t = next(iter(test_data))

# с использованием менеджера torch.no_grad вычислите прогнозы для выборки d
with torch.no_grad():
    # результат сохраните в тензоре predict
    predict = model(d.unsqueeze(-1)).squeeze()

# вычислите потери с помощью loss_func для predict и t; значение Q сохраните в виде вещественного числа
Q = loss_func(predict, t).item()
