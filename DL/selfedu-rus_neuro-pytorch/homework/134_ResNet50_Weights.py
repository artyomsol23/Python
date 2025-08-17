import torch
from torchvision import models


# здесь продолжайте программу
resnet_weights = models.ResNet50_Weights.DEFAULT

cats = resnet_weights.meta['categories']

print(cats[7])
