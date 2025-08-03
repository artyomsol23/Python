import numpy as np


def func(x):
    return 0.4 * x + 0.1 * np.sin(2*x) + 0.2 * np.cos(3*x)


# здесь объявляйте функцию df (производную) и продолжайте программу
def df(x):
    return 0.4 + 0.2 * np.cos(2 * x) - 0.6 * np.sin (3 * x)

eta = 1.0    # learning rate
x = 4.0
N = 500
gamma = 0.7  
v = 0.0      # начальное значение (импульс) 

for _ in range(N):
    v = gamma * v + (1 - gamma) * eta * df(x - gamma * v)
    x = x - v
