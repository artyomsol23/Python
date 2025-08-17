import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензора x)
class BlockEncode(nn.Module):
    def __init__(self):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(3, 16, (3, 3), stride=1, padding=1, bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(16),
            nn.Conv2d(16, 16, (3, 3), stride=1, padding=1, bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(16)
        )
        self.mp = nn.MaxPool2d(2)

    def forward(self, x):
        y1 = self.block(x)
        y2 = self.mp(y1)
        
        return y2, y1
    

x = torch.rand(3, 128, 128) # тензор x в программе не менять

# здесь продолжайте программу
model = BlockEncode()

model.eval()

with torch.no_grad():
    out1, out2 = model(x.unsqueeze(0))
