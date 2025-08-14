import numpy as np


x = list(map(int, input().split())) # чтение вектора [x1, x2] из входного потока

# здесь продолжайте программу
W1 = np.array([[1, 1]])
b1 = np.array([[-5]])

x = np.array([[x[0] ** 2, x[1] ** 2]])
y = W1 @ x.T + b1.T

print(f"{y.item():.1f}")
