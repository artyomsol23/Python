import torch
import torch.nn as nn


# здесь объявляйте классы BasicBlock1 и BasicBlock2
class BasicBlock1(nn.Module):
    def __init__(self):
        super().__init__()
        self.bn1 = nn.Sequential(
            nn.Conv2d(64, 128, (3, 3), padding=1, stride=2, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, (3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(128)
        )
        self.sc1 = nn.Sequential(
            nn.Conv2d(64, 128, (1, 1), padding=0, stride=2, bias=False),
            nn.BatchNorm2d(128)
        )

    def forward(self, x):
        return nn.functional.relu(self.bn1(x) + self.sc1(x))


class BasicBlock2(nn.Module):
    def __init__(self):
        super().__init__()
        self.bn2 = nn.Sequential(
            nn.Conv2d(128, 128, (3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.Conv2d(128, 128, (3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(128)
        )

    def forward(self, x):
        return nn.functional.relu(self.bn2(x) + x)

    
batch_size = 8
x = torch.rand(batch_size, 3, 32, 32) # тензор x в программе не менять

# здесь продолжайте программу
model = nn.Sequential(
    nn.Conv2d(3, 64, (7, 7), padding=3, stride=2, bias=False),
    nn.BatchNorm2d(64),
    nn.MaxPool2d((3, 3), stride=2, padding=1),
    BasicBlock1(),
    BasicBlock2(),
    nn.AdaptiveAvgPool2d((1, 1)),
    nn.Flatten(),
    nn.Linear(128, 10, bias=True)
)

model.eval()

predict = model(x)
