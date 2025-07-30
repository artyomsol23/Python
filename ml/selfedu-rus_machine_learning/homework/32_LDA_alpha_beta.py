import numpy as np

np.random.seed(0)

# исходные параметры распределений двух классов
mean1 = np.array([1, -2, 0])
mean2 = np.array([1, 3, 1])
r = 0.7
D = 2.0
V = [[D, D * r, D*r*r], [D*r, D, D*r], [D*r*r, D*r, D]]

# моделирование обучающей выборки
N = 1000
x1 = np.random.multivariate_normal(mean1, V, N).T
x2 = np.random.multivariate_normal(mean2, V, N).T

x_train = np.hstack([x1, x2]).T
y_train = np.hstack([np.zeros(N), np.ones(N)])

# здесь вычисляйте векторы математических ожиданий и ковариационную матрицу по выборке x1, x2
mm1 = np.mean(x1, axis=1)
mm2 = np.mean(x2, axis=1)

a = (x1.T - mm1).T
VV1 = np.array([[np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N, np.dot(a[0], a[2]) / N],
                [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N, np.dot(a[1], a[2]) / N],
                [np.dot(a[2], a[0]) / N, np.dot(a[2], a[1]) / N, np.dot(a[2], a[2]) / N]])

a = (x2.T - mm2).T
VV2 = np.array([[np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N, np.dot(a[0], a[2]) / N],
                [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N, np.dot(a[1], a[2]) / N],
                [np.dot(a[2], a[0]) / N, np.dot(a[2], a[1]) / N, np.dot(a[2], a[2]) / N]])

VV = (VV1 + VV2) / 2  # матрица ковариации

# параметры для линейного дискриминанта Фишера
Py1, L1 = 0.5, 1  # вероятности появления классов
Py2, L2 = 1 - Py1, 1  # и величины штрафов неверной классификации

# здесь продолжайте программу
alpha1 = np.linalg.inv(VV) @ mm1
alpha2 = np.linalg.inv(VV) @ mm2

beta1 = np.log(L1 * Py1) - 0.5 * mm1.T @ alpha1
beta2 = np.log(L2 * Py2) - 0.5 * mm2.T @ alpha2
