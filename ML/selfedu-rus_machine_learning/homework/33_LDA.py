import numpy as np

np.random.seed(0)

# исходные параметры распределений двух классов
mean1 = np.array([1, -2])
mean2 = np.array([-3, -1])
mean3 = np.array([1, 2])

r = 0.5
D = 1.0
V = [[D, D * r], [D*r, D]]

# моделирование обучающей выборки
N = 1000
x1 = np.random.multivariate_normal(mean1, V, N).T
x2 = np.random.multivariate_normal(mean2, V, N).T
x3 = np.random.multivariate_normal(mean3, V, N).T

x_train = np.hstack([x1, x2, x3]).T
y_train = np.hstack([np.zeros(N), np.ones(N), np.ones(N) * 2])

# здесь вычисляйте векторы математических ожиданий и ковариационную матрицу по выборке x1, x2, x3
mm1 = np.mean(x1, axis=1)
mm2 = np.mean(x2, axis=1)
mm3 = np.mean(x3, axis=1)

a = (x1.T - mm1).T
VV1 = np.array([[np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N],
                [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N]])

a = (x2.T - mm2).T
VV2 = np.array([[np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N],
                [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N]])

a = (x3.T - mm3).T
VV3 = np.array([[np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N],
                [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N]])

VV = (VV1 + VV2 + VV3) / 3  # матрица ковариации

# параметры для линейного дискриминанта Фишера
Py1, Py2, Py3 = 0.2, 0.4, 0.4
L1, L2, L3 = 1, 1, 1

# здесь продолжайте программу
alpha1 = np.linalg.inv(VV) @ mm1
alpha2 = np.linalg.inv(VV) @ mm2
alpha3 = np.linalg.inv(VV) @ mm3

beta1 = np.log(L1 * Py1) - 0.5 * mm1.T @ alpha1
beta2 = np.log(L2 * Py2) - 0.5 * mm2.T @ alpha2
beta3 = np.log(L3 * Py2) - 0.5 * mm3.T @ alpha3

b = lambda x, a, beta: x.T.dot(a) + beta

predict = [np.argmax([b(x, alpha1, beta1),
                      b(x, alpha2, beta2),
                      b(x, alpha3, beta3)]) for x in x_train]

Q = np.sum(predict != y_train)
