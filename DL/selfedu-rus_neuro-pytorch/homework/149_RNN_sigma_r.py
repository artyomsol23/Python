import torch
import torch.nn as nn


sigma_x, sigma_y = 0.1, 0.15                    # стандартные отклонения отсчетов последовательности
rx, ry = 0.9, 0.99                              # коэффициенты регрессии

sigma_noise_x = sigma_x * (1 - rx * rx) ** 0.5  # стандартное отклонение случайных величин
sigma_noise_y = sigma_y * (1 - ry * ry) ** 0.5  # стандартное отклонение случайных величин

# длина генерируемой последовательности
total = 100
# случайные величины, подаваемые на вход модели
noise = torch.randn((total, 2))
# начальное значение вектора скрытого состояния
h0 = torch.randn((1, 2)) * torch.tensor([sigma_noise_x, sigma_noise_y]) 

# здесь продолжайте программу
model = nn.RNN(input_size=2, hidden_size=2, bias=False, batch_first=True)

model.weight_hh_l0.data = torch.tensor([[rx, 0], [0, ry]], dtype=torch.float32)
model.weight_ih_l0.data = torch.tensor([[sigma_noise_x, 0], [0, sigma_noise_y]], dtype=torch.float32)

model.eval()

x, h = model(noise.view(1, total, 2),
             h0.view(1, 1, 2)
            )
