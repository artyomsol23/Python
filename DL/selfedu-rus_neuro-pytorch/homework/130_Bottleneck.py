import torch
import torch.nn as nn


# здесь объявляйте класс модели
class BottleneckBlock(nn.Module):
    def __init__(self):
        super().__init__()
        self.bn = nn.Sequential(
            nn.Conv2d(128, 64, (1, 1), stride=1, padding=0, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, (3, 3), stride=1, padding=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 256, (1, 1), stride=1, padding=0, bias=False),
            nn.BatchNorm2d(256)
        )
            
        self.sc = nn.Sequential(
            nn.Conv2d(128, 256, (1, 1), stride=1, padding=0, bias=False),  # padding = (kernel_size - 1) // 2
            nn.BatchNorm2d(256),
        )

    def forward(self, x):
        return nn.functional.relu(self.bn(x) + self.sc(x))

batch_size = 4
x = torch.rand(batch_size, 128, 16, 16) # тензор x в программе не менять

# здесь продолжайте программу
model_bn = BottleneckBlock()
model_bn.eval()

y = model_bn(x)
