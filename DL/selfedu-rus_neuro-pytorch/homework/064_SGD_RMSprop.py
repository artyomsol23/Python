import torch
import torch.optim as optim


def func(x):
    return 0.2 * (x - 2) ** 2 - 0.3 * torch.cos(4 * x)


lr = 0.1 # шаг обучения
x0 = 0.0 # начальное значение точки минимума
N = 200 # число итераций градиентного алгоритма

x = torch.tensor([x0], requires_grad=True)
optim = optim.RMSprop(params=[x], lr=lr)

for _ in range(N):
    y = func(x)
    
    optim.zero_grad()
    y.backward()          
    optim.step()
    
