import torch
import torch.nn as nn
from collections import OrderedDict


batch_size=12
x = torch.rand(batch_size, 64)  # тензор x в программе не менять

# здесь продолжайте программу
block_bm_dp = nn.Sequential(
    nn.Linear(32, 32, bias=False),
    nn.ELU(),
    nn.BatchNorm1d(32),
    nn.Dropout(0.3)
)

model = nn.Sequential(OrderedDict([
    ('input', nn.Linear(64, 32, bias=True)),
    ('act1', nn.ReLU()),
    ('block1', block_bm_dp),
    ('block2', block_bm_dp),
    ('block3', block_bm_dp),
    ('output', nn.Linear(32, 10, bias=True))
]))

model.eval()

predict = model(x)
