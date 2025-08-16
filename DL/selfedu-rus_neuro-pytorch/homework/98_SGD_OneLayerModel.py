import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


class FuncModel(nn.Module):
    def __init__(self):
        super().__init__()
        # модель однослойной полносвязной нейронной сети:
        # 1-й слой: число входов 4 (x, x^2, x^3, x^4), число нейронов 1
        self.layer1 = nn.Linear(4, 1)

    def forward(self, x):
        # реализация модели нейронной сети
        x.unsqueeze_(-1)
        xx = torch.cat([x, x ** 2, x ** 3, x ** 4], dim=1)
        y = self.layer1(xx)
        
        return y

    
torch.manual_seed(1)

model = FuncModel() # создать модель FuncModel

batch_size = 32 # размер батча

# создание обучающей выборки (значения функции)
data_x = torch.arange(-3, 3, 0.01) # тензоры data_x, data_y не менять
data_y = 0.2 * data_x ** 3 + 0.5 * torch.sin(5 * data_x) - 0.1 * data_x ** 2

# создание dataset
ds = data.TensorDataset(data_x, data_y)
# разделить ds на две части в пропорции: 80% на 20%
d_train, d_val = data.random_split(ds, [0.8, 0.2])
# создать объект класса DataLoader для d_train с размером пакетов batch_size и перемешиванием образов выборки
train_data = data.DataLoader(d_train, batch_size, shuffle=True)
# создать объект класса DataLoader для d_val с размером пакетов batch_size и без перемешивания образов выборки
train_data_val = data.DataLoader(d_val, batch_size, shuffle=False)

# создать оптимизатор Adam для обучения модели с шагом обучения 0.01
optimizer = optim.Adam(params=model.parameters(), lr=0.01)
# создать функцию потерь с помощью класса MSELoss
loss_func = nn.MSELoss()

loss_lst_val = []  # список значений потерь при валидации
loss_lst = []  # список значений потерь при обучении

epochs = 15 # число эпох обучения

for _ in range(epochs):
    loss_mean = 0 # вспомогательные переменные для вычисления среднего значения потерь при обучении
    lm_count = 0

    # обучение нейронной сети с вычисление средних потерь loss_mean
    for x, y in train_data:
        predict = model(x)
        loss = loss_func(predict, y.unsqueeze(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        lm_count += 1
        loss_mean = 1 / lm_count * loss.item() + (1 - 1 / lm_count) * loss_mean

    # валидация нейронной сети с вычислением средних потерь Q_val
    model.eval()
    
    Q_val = 0
    count_val = 0
    
    for x, y in train_data_val:
        with torch.no_grad():
            predict = model(x)
            loss = loss_func(predict, y.unsqueeze(-1))
            
            Q_val += loss.item()
            count_val += 1

    Q_val /= count_val
    
    # добавление в списки вычисленных значений потерь
    loss_lst.append(loss_mean)
    loss_lst_val.append(Q_val)
    
# перевести модель в режим эксплуатации
model.eval()
# выполнить прогноз модели по всем данным выборки
predict = model(data_x)
# вычислить потери с помощью loss_func по всем данным выборки ds; значение Q сохранить в виде вещественного числа
Q = loss_func(predict, data_y.unsqueeze(-1)).item()
