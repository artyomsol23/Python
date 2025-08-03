import numpy as np


def func(x):
    return 0.1 * x - np.cos(x/2) + 0.4 * np.sin(3*x) + 5


np.random.seed(0)

x = np.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
y = func(x) + np.random.normal(0, 0.2, len(x)) # значения функции по оси ординат

# здесь продолжайте программу
h = 1.0
K = lambda r: np.exp(-2 * r * r)     # гауссовское парзеновское окно
ro = lambda xx, xi: np.abs(xx - xi)  # модуль разностей
w = lambda xx, xi: K(ro(xx, xi) / h)

y_est = []

for xx in x:
    ww = np.array([w(xx, xi) for xi in x])
    
    yy = np.dot(ww, y) / sum(ww)
    y_est.append(yy)
    
Q = np.mean((np.array(y_est) - y) ** 2)
