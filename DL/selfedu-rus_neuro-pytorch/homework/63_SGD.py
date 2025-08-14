import torch


def func(x):
    return 0.2 * (x - 2) ** 2 - 0.3 * torch.cos(4 * x)


x0 = 0.0 # начальное значение точки минимума
lr = 0.1 # шаг обучения
N = 200 # число итераций градиентного алгоритма
x = torch.tensor([x0], requires_grad=True)

for _ in range(N):
    y = func(x)
    y.backward()
    
    x.data -= lr * x.grad
    x.grad.zero_()
  
