import torch


def model(w0, w1, w2, w3, x):
    return w0 + w1 * x + w2 * x ** 2 + w3 * x ** 3


def func(x):
    return 0.5 * x ** 2 - 2 * x - 5


xx = float(input()) # значение xx в программе не менять
x = torch.tensor(xx, dtype=torch.float32)

x0, x1, x2, x3 = map(float, input().split()) # переменные x0, x1, x2, x3 в программе не менять

w0 = torch.tensor([x0], dtype=torch.float32, requires_grad=True)
w1 = torch.tensor([x1], dtype=torch.float32, requires_grad=True)
w2 = torch.tensor([x2], dtype=torch.float32, requires_grad=True)
w3 = torch.tensor([x3], dtype=torch.float32, requires_grad=True)

L = (model(w0, w1, w2, w3, x) - func(x)) ** 2
L.backward()
