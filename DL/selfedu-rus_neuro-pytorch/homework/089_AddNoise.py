from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms.v2 as tfs_v2


# здесь объявляйте класс AddNoise
class AddNoise(nn.Module):
    def __init__(self, volume):
        super().__init__()
        self.volume = volume
        
    def forward(self, x):
        noise = torch.randn_like(x) * self.volume
        x = x.to(torch.float32) + noise
        
        return x


img_pil = Image.new(mode="RGB", size=(128, 128), color=(0, 128, 255))

# здесь продолжайте программу
transforms = tfs_v2.Compose([tfs_v2.ToTensor(), AddNoise(0.1)])

img = transforms(img_pil)
