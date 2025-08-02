import numpy as np


def func(x):
    return 0.5 * x**2 - 0.1 * 1/np.exp(-x) + 0.5 * np.cos(2*x) - 2.


# здесь объявляйте дополнительные функции (если необходимо)
def model(x, w):
    return w[0] + w[1] * x + w[2] * x ** 2 + w[3] * np.cos(2 * x) + w[4] * np.sin(2 * x)


coord_x = np.arange(-5.0, 5.0, 0.1) # значения отсчетов по оси абсцисс
coord_y = func(coord_x) # значения функции по оси ординат

sz = len(coord_x) # общее число отсчетов

# здесь продолжайте программу
w = [-1.59, -0.69, 0.278, 0.497, -0.106]

predicted = model(coord_x, w)
loss = np.abs(predicted - coord_y)

Q = np.mean(loss)
