import torch


# значения списков w и g в программе не менять
w = list(map(float, input().split()))
g = list(map(float, input().split()))
t_inp = torch.rand(3) * 10

W1 = torch.tensor(w, dtype=torch.float32).view(2, -1)
W1 = W1[:, 1:]
bias1 = W1[:, 0]

W2 = torch.tensor(g[1:], dtype=torch.float32)[1:]
bias2 = torch.tensor(g[0], dtype=torch.float32)

u = (W1 @ t_inp + bias1).sigmoid()
y = W2 @ u + bias2
