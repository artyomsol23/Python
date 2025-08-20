import torch
import torch.nn as nn


# здесь объявляйте класс VAE
class VAE(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden_dim = 4
        self.encoder = nn.Sequential(
            nn.Linear(
                in_features=128,
                out_features=32,
                bias=False,
            ),
            nn.BatchNorm1d(32),
            nn.ReLU(inplace=True),
            nn.Linear(
                    in_features=32,
                    out_features=8,
                    bias=False,
            ),
            nn.BatchNorm1d(8),
            nn.ReLU(inplace=True),
        )
        self.h_mean = nn.Sequential(
            nn.Linear(
                    in_features=8,
                    out_features=self.hidden_dim,
                    bias=True
            )
        )
        self.h_var = nn.Linear(
                in_features=8,
                out_features=self.hidden_dim,
                bias=True
        )
        self.decoder = nn.Sequential(
            nn.Linear(
                    in_features=self.hidden_dim,
                    out_features=64,
                    bias=True,
            ),
            nn.ReLU(inplace=True),
            nn.Linear(
                in_features=64,
                out_features=128,
                bias=True
            ),
        )

    def forward(self, x):
        enc = self.encoder(x)

        h_mean = self.h_mean(enc)
        h_var = torch.relu(self.h_var(enc))

        noise = torch.normal(mean=torch.zeros_like(h_mean), std=torch.ones_like(h_var))
        h = noise * torch.sqrt(h_var) + h_mean
        x = self.decoder(h)

        return x, h_mean, h_var


# тензор data_x в программе не менять
batch_size = 8
data_x = torch.rand(batch_size, 128)

# здесь создавайте модель и продолжайте программу
model = VAE()

model.eval()

out, hm, hv = model(data_x)
