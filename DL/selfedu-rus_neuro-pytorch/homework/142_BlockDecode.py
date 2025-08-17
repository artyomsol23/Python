import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензоров)
class BlockDecode(nn.Module):
    def __init__(self):
        super().__init__()
        self.tr = nn.ConvTranspose2d(32, 16, (2, 2), stride=2, padding=0, bias=True)
        self.block = nn.Sequential(
            nn.Conv2d(32, 16, (3, 3), stride=1, padding=1, bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(16),
            nn.Conv2d(16, 16, (3, 3), stride=1, padding=1, bias=False),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(16)
        )
        self.out = nn.Conv2d(16, 1, (1, 1), stride=1, padding=0, bias=True)

    def forward(self, x, y):
        x = self.tr(x)
        x = torch.cat([x, y], dim=1)
        x = self.block(x)
        
        return self.out(x)
    

# тензоры x, y в программе не менять
batch_size = 2
x = torch.rand(batch_size, 32, 32, 32)
y = torch.rand(batch_size, 16, 64, 64)

# здесь продолжайте программу
model = BlockDecode()

model.eval()

with torch.no_grad():
    out = model(x, y)
