from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as tfs


# здесь объявляйте класс VAE_CNN
class VAE_CNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden_dim = 7
        self.encoder = nn.Sequential(
            nn.Conv2d(
                in_channels=3,
                out_channels=16,
                kernel_size=(3, 3),
                stride=1,
                padding=1,
                groups=1,
                bias=True,
                dilation=1,
            ),
            nn.ELU(inplace=True),
            nn.MaxPool2d(
                kernel_size=(3, 3),
                stride=2,
                padding=0,
                dilation=1,
                return_indices=False,
                ceil_mode=False
            ),
            nn.Conv2d(
                in_channels=16,
                out_channels=4,
                kernel_size=(3, 3),
                stride=1,
                padding=1,
                groups=1,
                bias=True,
                dilation=1,
            ),
            nn.ELU(inplace=True),
            nn.MaxPool2d(
                kernel_size=(3, 3),
                stride=2,
                padding=0,
                dilation=1,
                return_indices=False,
                ceil_mode=False
                ),
            nn.Flatten()
        )
        self.h_mean = nn.Linear(
            in_features=36,
            out_features=self.hidden_dim,
            bias=True
        )
        self.h_log_var = nn.Linear(
            in_features=36,
            out_features=self.hidden_dim,
            bias=True
        )
        self.decoder = nn.Sequential(
            nn.Linear(
                in_features=self.hidden_dim,
                out_features=32,
                bias=True,
            ),
            nn.ReLU(inplace=True),
            nn.Unflatten(
                dim=1,
                unflattened_size=(2, 4, 4)
            ),
            nn.ConvTranspose2d(
                in_channels=2,
                out_channels=8,
                kernel_size=(2, 2),
                stride=2,
                padding=0,
                groups=1,
                bias=True,
                dilation=1,
            ),
            nn.ReLU(inplace=True),
            nn.ConvTranspose2d(
                in_channels=8,
                out_channels=1,
                kernel_size=(2, 2),
                stride=2,
                padding=0,
                groups=1,
                bias=True,
                dilation=1,
            ),
            nn.Sigmoid()
        )

    def forward(self, x):
        enc = self.encoder(x)

        h_mean = self.h_mean(enc)
        h_log_var = self.h_log_var(enc)

        noise = torch.normal(mean=torch.zeros_like(h_mean), std=torch.ones_like(h_log_var))
        h = noise * torch.exp(h_log_var / 2) + h_mean
        x = self.decoder(h)

        return x, h_mean, h_log_var


img_pil = Image.new(mode="RGB", size=(64, 78), color=(0, 128, 255))

# здесь продолжайте программу
tr = tfs.Compose([tfs.CenterCrop(64), tfs.Resize(16), tfs.ToTensor()])
img = tr(img_pil)

model = VAE_CNN()

model.eval()

out, hm, hlv = model(img.unsqueeze(0))
