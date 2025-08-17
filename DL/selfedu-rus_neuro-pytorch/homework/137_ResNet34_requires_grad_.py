import torch
from torchvision import models
import torchvision.transforms.functional as TF


# тензор x и img_pil в программе не менять
x = torch.randint(0, 255, (3, 100, 100), dtype=torch.float32) 
img_pil = TF.to_pil_image(x)

# здесь продолжайте программу
weights = models.ResNet34_Weights.DEFAULT
transforms = weights.transforms()

model = models.resnet34()
model.requires_grad_(False)

model.eval()

img = transforms(img_pil)

results = model(img.unsqueeze(0))
