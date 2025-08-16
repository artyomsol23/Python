import numpy as np
import torch
import torch.optim as optim


n_features = 4 # число коэффициентов w
x = torch.arange(-3, 3, 0.1)
y_train = -0.1 * x + 0.2 * torch.sin(2 * x) - 0.1 * torch.cos(5 * x)
x_train = torch.tensor([[_x ** _n for _n in range(n_features)] for _x in x])

w = torch.FloatTensor(n_features).uniform_(-1e-5, 1e-5)
w.requires_grad_(True)

total = len(y_train)
lr = 0.01 # шаг обучения
N = 1000 # число итераций алгоритма SGD

np.random.seed(1) # установка "зерна" генератора датчика случайных чисел

# здесь продолжайте программу
loss = torch.nn.MSELoss()
optim = optim.RMSprop(params=[w], lr=lr)

for _ in range(N):
    k = np.random.randint(0, total)
    y = x_train[k] @ w
    loss_k = loss(y, y_train[k])

    optim.zero_grad()
    loss_k.backward()
    optim.step()
    
Q = torch.mean(((x_train @ w) - y_train) ** 2).item()
