import torch


d = float(input()) # значение d в программе не менять
t = torch.tensor([d], requires_grad=True)

s = 3 * t ** 2 + 5 * t - 2
s.backward()
