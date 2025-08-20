import torch
import torch.nn as nn


class AutoEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(
            in_features=2,
            out_features=1,
            bias=True)
        self.output = nn.Linear(
            in_features=1,
            out_features=2,
            bias=True)

    def forward(self, x):
        x = self.hidden(x)
        return self.output(x)


model_ae = AutoEncoder()

model_ae.hidden.weight.data = torch.tensor([[1.0, 0.0]])    # h = w1 * x + w2 * y + b
model_ae.hidden.bias.data = torch.tensor([0.0])             # оставляем только x

model_ae.output.weight.data = torch.tensor([[1.0], [3/7]])  # k = 3/7
model_ae.output.bias.data = torch.tensor([0.0, 3.0])        # y = kx + b -> b = 3
