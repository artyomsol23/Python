import torch
import torch.nn as nn


# здесь объявляйте классы BottleneckBlock1 и BottleneckBlock2
class BottleneckBlock1(nn.Module):
    def __init__(self):
        super().__init__()
        self.bn = nn.Sequential(
            nn.Conv2d(64, 64, (1, 1), padding=0, stride=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, (3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 256, (1, 1), padding=0, stride=1, bias=False),
            nn.BatchNorm2d(256)
        )
        self.sc = nn.Sequential(
            nn.Conv2d(64, 256, (1, 1), padding=0, stride=1, bias=False),
            nn.BatchNorm2d(256)
        )

    def forward(self, x):
        return nn.functional.relu(self.bn(x) + self.sc(x))


class BottleneckBlock2(nn.Module):
    def __init__(self):
        super().__init__()
        self.bn = nn.Sequential(
            nn.Conv2d(256, 64, (1, 1), padding=0, stride=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 64, (3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.Conv2d(64, 256, (1, 1), padding=0, stride=1, bias=False),
            nn.BatchNorm2d(256)
        )

    def forward(self, x):
        return nn.functional.relu(self.bn(x) + x)


batch_size = 8
x = torch.rand(batch_size, 3, 32, 32) # тензор x в программе не менять

# здесь продолжайте программу
model = nn.Sequential(
    nn.Conv2d(3, 64, (7, 7), padding=3, stride=2, bias=False),
    nn.BatchNorm2d(64),
    nn.MaxPool2d((3, 3), padding=1, stride=2),
    BottleneckBlock1(),
    BottleneckBlock2(),
    nn.AdaptiveAvgPool2d((1, 1)),
    nn.Flatten(),
    nn.Linear(256, 10)
)

model.eval()

predict = model(x)
