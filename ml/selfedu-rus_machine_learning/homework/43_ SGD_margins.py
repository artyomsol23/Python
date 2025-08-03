import numpy as np
from sklearn.model_selection import train_test_split


def loss(w, x, y):
    # здесь реализация экспоненциальной функции потерь
    M = np.dot(w, x) * y
    
    return np.exp(-M)


def df(w, x, y):
    # здесь реализация производной функции потерь по вектору w
    M = np.dot(w, x) * y
    
    return -np.exp(-M) * x * y


np.random.seed(0)

# исходные параметры распределений двух классов
r1 = 0.4
D1 = 2.0
mean1 = [1, -2]
V1 = [[D1, D1 * r1], [D1 * r1, D1]]

r2 = 0.5
D2 = 3.0
mean2 = [2, 3]
V2 = [[D2, D2 * r2], [D2 * r2, D2]]

# моделирование обучающей выборки
N = 1000
x1 = np.random.multivariate_normal(mean1, V1, N).T
x2 = np.random.multivariate_normal(mean2, V2, N).T

data_x = np.array([[1, x[0], x[1]] for x in np.hstack([x1, x2]).T])
data_y = np.hstack([np.ones(N) * -1, np.ones(N)])

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, random_state=123,test_size=0.3, shuffle=True)

n_train = len(x_train)  # размер обучающей выборки
w = [0.0, 0.0, 0.0]  # начальные весовые коэффициенты
nt = np.array([0.5, 0.01, 0.01])  # шаг обучения для каждого параметра w0, w1, w2
N = 500  # число итераций алгоритма SGD
batch_size = 10 # размер мини-батча (величина K = 10)

# здесь продолжайте программу
for _ in range(N):
    k = np.random.randint(0, n_train - batch_size)  # n_train - размер выборки (массива x_train)
    grad = np.zeros_like(w)
    
    for i in range(k, k + batch_size):
        grad += df(w, x_train[i], y_train[i])
    
    grad /= batch_size
    w -= nt * grad
    
mrgs = np.array([np.dot(w, x) * y for x, y in zip(x_test, y_test)])
mrgs = np.sort(mrgs)

predict = np.array([1 if np.dot(w, x) >= 0 else -1 for x in x_test])

acc = np.mean(predicti == y_test)
