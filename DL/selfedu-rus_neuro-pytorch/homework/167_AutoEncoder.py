import torch
import torch.nn as nn


# здесь объявляйте класс модели (обязательно до тензора)
class AutoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(
                in_channels=3,
                out_channels=8,
                kernel_size=(3,3),
                stride=2,
                padding=1,
                groups=1,
                bias=False,
            ),
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(8),
            nn.Conv2d(
                in_channels=8,
                out_channels=4,
                kernel_size=(3,3),
                stride=2,
                padding=1,
                groups=1,
                bias=False,
            ),            
            nn.ReLU(inplace=True),
            nn.BatchNorm2d(4),
            nn.Flatten(
                start_dim=1,
                end_dim=-1
            ),
            nn.Linear(
                in_features=64,
                out_features=4,
                bias=True
            ),
            nn.ReLU(inplace=True)
        )

        self.decoder = nn.Sequential(
            nn.Linear(
                in_features=4,
                out_features=64,
                bias=True
            ),
            nn.ELU(inplace=True),
            nn.Unflatten(
                dim=1,
                unflattened_size=(4, 4, 4)
            ),
            nn.ConvTranspose2d(
                    in_channels=4,
                    out_channels=8,
                    kernel_size=(2, 2),
                    stride=2,
                    padding=0,
                    output_padding=0,
                    groups=1,
                    bias=True,
                    dilation=1,
            ),
            nn.ELU(inplace=True),
            nn.ConvTranspose2d(
                    in_channels=8,
                    out_channels=1,
                    kernel_size=(2 ,2),
                    stride=2,
                    padding=0,
                    output_padding=0,
                    groups=1,
                    bias=True,
                    dilation=1,
            )
        )

    def forward(self, x):
        h = self.encoder(x)
        return self.decoder(h), h


h = torch.rand(4) # тензор h в программе не менять

# здесь продолжайте программу
model = AutoEncoder()

model.eval()

model.load_state_dict(st_model)
out = model.decoder(h.unsqueeze(0))
