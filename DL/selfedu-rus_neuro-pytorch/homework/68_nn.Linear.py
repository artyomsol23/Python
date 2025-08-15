import torch
import torch.nn as nn


# тензор x в программе не менять
x = torch.tensor(list(map(float, input().split())), dtype=torch.float32)

# здесь продолжайте программу
layer = nn.Linear(16, 1, bias=False)
layer.weight.data = torch.ones(1, 16)

y = layer(x)

print(f'{y.item():.1f}')
