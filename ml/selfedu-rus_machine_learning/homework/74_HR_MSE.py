import numpy as np

x = np.arange(-2, 3, 0.1)
y = -x + 0.2 * x ** 2 - 0.5 * np.sin(4*x) + np.cos(2*x)

# здесь продолжайте программу
t = 0

left_i = np.where(x < t)[0]
right_i = np.where(x >= t)[0]

y1, y2 = y[left_i], y[right_i]
b, b1, b2 = np.mean(y), np.mean(y1), np.mean(y2)

# MSE
HR = np.sum((b - y) ** 2)
HR1 = np.sum((b1 - y1) ** 2)
HR2 = np.sum((b2 - y2) ** 2)

N0, N1, N2 = len(y), len(y1), len(y2)

IG = HR - (((N1 / N0) * HR1) + ((N2 / N0) * HR2))
