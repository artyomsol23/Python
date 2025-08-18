import torch
import torch.nn as nn


N = 200  # размер генерируемой последовательности
r = 0.95 # коэффициент регрессии
std = 10 # стандартное отклонение sigma
std_e = std * (1 - r * r) ** 0.5 # стандартное отклонение случайных добавок

x = torch.empty(N, dtype=torch.float32)
x[0] = torch.randn(1) * std

# здесь продолжайте программу
for t in range(1, N):
    x[t] = r * x[t - 1] + torch.randn(1) * std_e
