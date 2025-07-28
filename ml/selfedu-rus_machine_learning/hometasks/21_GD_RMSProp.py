import numpy as np


def func(x):
    return 2 * x + 0.1 * x ** 3 + 2 * np.cos(3*x)


# здесь объявляйте функцию df (производную) и продолжайте программу
def df(x):
    return 2 + 0.3 * x ** 2 - 6 * np.sin(3 * x)

eta = 0.5
x = 4
N = 200
alpha = 0.8
G = 0  # начальное значение
epsilon = 0.01

for _ in range(N):
    grad = df(x)
    G = alpha * G + (1 - alpha) * grad ** 2
    x -= eta * grad / (np.sqrt(G) + epsilon)
