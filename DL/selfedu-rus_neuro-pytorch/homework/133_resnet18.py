import torch
import torch.nn as nn
from torchvision import models


x = torch.rand(3, 224, 224) # тензор x в программе не менять

# здесь продолжайте программу (в том числе и создавайте модель)
model = models.resnet18()

model.eval()

out = model(x.unsqueeze(0))
