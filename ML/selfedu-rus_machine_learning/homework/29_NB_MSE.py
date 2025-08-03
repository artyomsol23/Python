import numpy as np


def func(x):
    return 0.5 * x + 0.2 * x ** 2 - 0.05 * x ** 3 + 0.2 * np.sin(4 * x) - 2.5


def model(w, x):
    return w[0] + w[1] * x + w[2] * x ** 2 + w[3] * x ** 3


coord_x = np.arange(-4.0, 6.0, 0.1)

x_train = np.array([[_x**i for i in range(4)] for _x in coord_x]) # обучающая выборка
y_train = func(coord_x) # целевые выходные значения

# здесь продолжайте программу
X, y = x_train, y_train

w = np.linalg.inv(X.T @ X) @ X.T @ y  # нормальное уравнение линейной регрессии

a_x = model(w, coord_x)
f_x = func(coord_x)

Q = np.mean((f_x - a_x) ** 2)  # MSE
