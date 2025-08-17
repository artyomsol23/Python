import torch
import torchvision.transforms as tfs
import torch.nn as nn


# здесь продолжайте программу
model = nn.Sequential(
    nn.Conv2d(3, 64, (3, 3), stride=1, padding=1, bias=True),
    nn.ReLU(inplace=True),
    nn.Conv2d(64, 64, (3, 3), stride=1, padding=1, bias=True),
    nn.ReLU(inplace=True),
    nn.MaxPool2d((2, 2), stride=2),
    nn.Conv2d(64, 128, (3, 3), stride=1, padding=1, bias=True),
    nn.ReLU(inplace=True),
    nn.Conv2d(128, 128, (3, 3), stride=1, padding=1, bias=True),
    nn.ReLU(inplace=True),
    nn.MaxPool2d((2, 2), stride=2)
)

transforms = tfs.Compose([
    tfs.Resize((224, 224)),
    tfs.ToTensor()
])

img = transforms(img_pil)

model.eval()

out = model(img.unsqueeze(0))
