import torch
import torch.nn as nn
import torchvision.transforms.v2 as tfs_v2


# здесь объявляйте класс ToDtypeV1
class ToDtypeV1(nn.Module):
    def __init__(self, dtype, scale=False):
        super().__init__()
        self.dtype = dtype
        self.scale = scale
        
    def forward(self, x):
        x = x.to(self.dtype)
        if self.scale and self.dtype in (torch.float16, torch.float32, torch.float64):
            xmin = x.min()
            xmax = x.max()
            x = (x - xmin) / xmax
            
        return x


H, W = 128, 128
img_orig = torch.randint(0, 256, size=(3, H, W), dtype=torch.uint8) # тензор в программе не менять

# средние для каждого цветового канала (первая ось)
img_mean = torch.mean(img_orig.float(), [1, 2])
# стандартное отклонение для каждого цветового канала (первая ось)
img_std = torch.std(img_orig.float().flatten(1, 2), dim=1)

# здесь продолжайте программу
transforms = tfs_v2.Compose([ToDtypeV1(dtype=torch.float32, scale=False),
                        tfs_v2.Normalize(mean=img_mean, std=img_std)
                        ])

img = transforms(img_orig)
