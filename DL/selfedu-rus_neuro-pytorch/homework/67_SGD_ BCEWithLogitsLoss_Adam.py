import numpy as np
import torch
import torch.optim as optim


def model(x, w1, w2, b1, b2):
    x = w1 @ x + b1
    x = torch.tanh(x)
    x = w2 @ x + b2
    return x


np.random.seed(1) # установка "зерна" генератора датчика случайных чисел
torch.manual_seed(123)

W1 = torch.empty(2, 2).normal_(0, 1e-5)
bias1 = torch.rand(2, requires_grad=True)
W2 = torch.empty(1, 2).normal_(0, 1e-5)
bias2 = torch.rand(1, requires_grad=True)

W1.requires_grad_(True)
W2.requires_grad_(True)

# обучающая выборка
n_items = 20
C00 = torch.empty(n_items, 2).normal_(0, 1)
C11 = torch.empty(n_items, 2).normal_(0, 1) + torch.FloatTensor([5, 5])
C01 = torch.empty(n_items, 2).normal_(0, 1) + torch.FloatTensor([0, 5])
C10 = torch.empty(n_items, 2).normal_(0, 1) + torch.FloatTensor([5, 0])

x_train = torch.cat([C00, C11, C01, C10])
y_train = torch.cat([torch.ones(n_items * 2), torch.zeros(n_items * 2)])

lr = 0.01  # шаг обучения
N = 1000  # число итераций при обучении
total = y_train.size(0) # размер обучающей выборки

# здесь продолжайте программу
loss_func = torch.nn.BCEWithLogitsLoss()
optim = optim.Adam(params=[W1, W2, bias1, bias2], lr=lr)

for _ in range(N):
    k = np.random.randint(0, total)
    predict = model(x_train[k], W1, W2, bias1, bias2)
    y = loss_func(predict, y_train[k].unsqueeze(0))  # добавить доп. ось
    
    y.backward()
    optim.step()
    optim.zero_grad()

Q = 0

for x, d in zip(x_train, y_train):
    Q += (torch.sign(model(x, W1, W2, bias1, bias2)) == (d * 2 - 1)).float().item()

Q /= (n_items * 4)
