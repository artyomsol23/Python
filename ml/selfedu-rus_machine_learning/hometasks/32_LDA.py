import numpy as np

np.random.seed(0)

# исходные параметры распределений двух классов
mean1 = [1, -2]
mean2 = [1, 3]
r = 0.7
D = 2.0
V = [[D, D * r], [D * r, D]]

# моделирование обучающей выборки
N = 1000
x1 = np.random.multivariate_normal(mean1, V, N).T
x2 = np.random.multivariate_normal(mean2, V, N).T

x_train = np.hstack([x1, x2]).T
y_train = np.hstack([np.ones(N) * -1, np.ones(N)])

# вычисление оценок МО и ковариационной матрицы
mm1 = np.mean(x1.T, axis=0)
mm2 = np.mean(x2.T, axis=0)

a = np.hstack([(x1.T - mm1).T, (x2.T - mm2).T])
VV = np.array([[np.dot(a[0], a[0]) / (2*N), np.dot(a[0], a[1]) / (2*N)],
                [np.dot(a[1], a[0]) / (2*N), np.dot(a[1], a[1]) / (2*N)]])

# здесь продолжайте программу
lm = 1
P = 0.5

# LDA
b = lambda x, v, m, l, py: (np.log(l * py) - 0.5 * m @ np.linalg.inv(v) @ m + x @ np.linalg.inv(v) @ m)

predict = []

for x in x_train:
    d1 = b(x, VV, mm1, lm, P)
    d2 = b(x, VV, mm2, lm, P)
    
    predict.append(-1 if d1 > d2 else 1)

Q = np.sum(predict != y_train)
