import torch


g = float(input()) # значение g в программе не менять
d = float(input()) # значение d в программе не менять

G = torch.tensor([g], dtype=torch.float32)
t = torch.tensor([d], dtype=torch.float32, requires_grad=True)

v = -G * t ** 2 / 2 + G * torch.exp(-t) + 1.5
v.backward()
