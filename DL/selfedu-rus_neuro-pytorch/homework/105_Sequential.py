import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


# пропишите модель нейронной сети
model = nn.Sequential(
    nn.Linear(3, 1),
)

# создание обучающей выборки
_x = torch.arange(-5, 5, 0.1)
data_y = torch.sin(2 * _x) + 0.2 * torch.cos(10 * _x) + 0.1 * _x ** 2

_x.unsqueeze_(-1)
data_x = torch.cat([_x, _x ** 2, _x ** 3], dim=1)
ds = data.TensorDataset(data_x, data_y)

batch_size = 8 # размер батча

# создать объект класса DataLoader для датасета ds с размером пакетов batch_size и перемешиванием образов выборки
train_data = data.DataLoader(ds, batch_size, shuffle=True)

# создать оптимизатор RMSprop для обучения модели с шагом обучения 0.01
optimizer = optim.RMSprop(params=model.parameters(), lr=0.01)
# создать функцию потерь с помощью класса MSELoss
loss_func = torch.nn.MSELoss()

epochs = 20 # число эпох обучения

# перевести модель в режим обучения
model.train()

for _ in range(epochs): # итерации по эпохам
    for x_train, y_train in train_data:
        # вычислить прогноз модели для данных x_train
        predict = model(x_train)
        # вычислить значение функции потерь
        loss = loss_func(predict, y_train.unsqueeze(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# перевести модель в режим эксплуатации
model.eval()
# выполнить прогноз модели по всем данным выборки
predict = model(data_x)
# вычислить потери с помощью loss_func по всем данным выборки; значение Q сохранить в виде вещественного числа
Q = loss_func(predict, data_y.unsqueeze(-1)).item()
