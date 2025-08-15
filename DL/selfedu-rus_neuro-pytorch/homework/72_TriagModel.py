import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim


# здесь объявляйте класс TriagModel
class TriagModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Linear(3, 1, bias=False)
    
    def forward(self, x):
        x = self.layer(x)
        
        return x


np.random.seed(1)
torch.manual_seed(1)

total = 100
x_train = torch.randint(1, 10, (total, 3), dtype=torch.float32)
y_train = x_train.sum(dim=1) / 3

# здесь создавайте модель (model)
model = TriagModel()
# переведите модель в режим обучения
model.train()

lr = 0.01 # шаг обучения
N = 1000 # число итераций SGD

# здесь сформируйте оптимизатор Adam с параметрами модели и шагом обучения lr
optimizer = optim.Adam(params=model.parameters(), lr=lr)
# здесь создайте функцию потерь с помощью класса nn.MSELoss
loss_func = nn.MSELoss()

for _ in range(N):
    k = np.random.randint(0, total)
    # пропустите через модель k-й образ выборки x_train и вычислите прогноз predict
    predict = model(x_train[k])
    # вычислите значение функции потерь и сохраните результат в переменной loss
    loss = loss_func(predict, y_train[k])

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
