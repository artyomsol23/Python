import numpy as np

np.random.seed(0)

# исходные параметры распределений двух классов
r1 = 0.7
D1 = 1.0
mean1 = [-1, -2, -1]
V1 = [[D1, D1 * r1, D1*r1*r1], [D1 * r1, D1, D1*r1], [D1*r1*r1, D1*r1, D1]]

r2 = 0.5
D2 = 2.0
mean2 = [1, 2, 1]
V2 = [[D2, D2 * r2, D2*r2*r2], [D2 * r2, D2, D2*r2], [D2*r2*r2, D2*r2, D2]]

# моделирование обучающей выборки
N = 1000
x1 = np.random.multivariate_normal(mean1, V1, N).T
x2 = np.random.multivariate_normal(mean2, V2, N).T

x_train = np.hstack([x1, x2]).T
y_train = np.hstack([np.ones(N) * -1, np.ones(N)])

# здесь продолжайте программу
mm1, mm2 = np.mean(x1.T, axis=0), np.mean(x2.T, axis=0)  # NB! x1.T <= если прописать x1 (без ".T"), то axis=1
VV1, VV2 = np.cov(x1, rowvar=True), np.cov(x2, rowvar=True)

Py1, L1 = 0.5, 1
Py2, L2 = 0.5, 1

b = lambda x, v, m, l, py: np.log(l * py) - 0.5 * (x - m) @ np.linalg.inv(v) @ (x - m).T - 0.5 * np.log(np.linalg.det(v))

predict = []

for x in x_train:
    d1 = b(x, VV1, mm1, L1, Py1)
    d2 = b(x, VV2, mm2, L2, Py2)
    
    predict.append(-1 if d1 > d2 else 1)

Q = np.sum(predict != y_train)
