import numpy as np


def func(x):
    return 0.5 * x + 0.2 * x ** 2 - 0.1 * x ** 3

def df(x):
    return 0.5 + 0.4 * x - 0.3 * x ** 2  # здесь выражение производной функции f(x)


coord_x = np.arange(-5.0, 5.0, 0.1)  # значения по оси абсцисс
coord_y = func(coord_x)  # значения по оси ординат (значения функции)

# здесь продолжайте программу
eta = 0.01
x = -4
n = 200

for _ in range(n):
    x = x - eta * df(x)
