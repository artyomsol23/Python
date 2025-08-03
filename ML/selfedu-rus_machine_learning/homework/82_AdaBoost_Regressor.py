import numpy as np
from sklearn.tree import DecisionTreeRegressor


x = np.arange(-3, 3, 0.1).reshape(-1, 1)
y = 2 * np.cos(x) + 0.5 * np.sin(2*x) - 0.2 * np.sin(4*x)

# здесь продолжайте программу
T = 6                    # число алгоритмов в композиции
max_depth = 3            # максимальная глубина решающих деревьев
algs = []                # список из полученных алгоритмов
s = np.array(y.ravel())

for n in range(T):
    b_t = DecisionTreeRegressor(max_depth=max_depth)  # создаем дерево
    b_t.fit(x, s)                                     # обучаем на текущих остатках
    algs.append(b_t)                                  # сохраняем обученную модель

    s -= b_t.predict(x)                               # обновляем остатки, вычитая предсказания модели

yy = algs[0].predict(x)

for n in range(1, T):
    yy += algs[n].predict(x)

QT = np.mean((yy - y.ravel()) ** 2)  # размерность!!!
