import numpy as np

# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.5 * x ** 2 - 0.1 * 1 / np.exp(-x) + 0.5 * np.cos(2 * x) - 2.


# здесь объявляйте необходимые функции
def a(x, w):
    return w[0] + w[1] * x + w[2] * x ** 2 + w[3] * np.cos(2 * x) + w[4] * np.sin(2 * x)

def gradient(x, y, w):
    x_vec = np.array([1, x, x ** 2, np.cos(2 * x), np.sin(2 * x)])
    return 2 * (a(x, w) - y) * x_vec

def loss(x, y, w):
    return (a(x, w) - y) ** 2


coord_x = np.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = len(coord_x)	# количество значений функций (точек)
eta = np.array([0.01, 0.001, 0.0001, 0.01, 0.01]) # шаг обучения для каждого параметра w0, w1, w2, w3, w4
w = np.array([0., 0., 0., 0., 0.]) # начальные значения параметров модели
N = 500 # число итераций алгоритма SGD
lm = 0.02 # значение параметра лямбда для вычисления скользящего экспоненциального среднего

Qe = 0.0 # начальное значение среднего эмпирического риска
np.random.seed(0) # генерация одинаковых последовательностей псевдослучайных чисел

for _ in range(N):
    k = np.random.randint(0, sz)
    x_k = coord_x[k]
    y_k = coord_y[k]
    
    grad = gradient(xk, yk, w)
    w -= eta * grad
    
    Lk = loss(xk, yk, w)
    Qe = lm * Lk + (1 - lm) * Qe

total_loss = 0.0

for i in range(sz):
    xi = coord_x[i]
    yi = coord_y[i]
    total_loss += loss(xi, yi, w)

Q = total_loss / sz
