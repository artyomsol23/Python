import numpy as np

# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.02 * np.exp(-x) - 0.2 * np.sin(3 * x) + 0.5 * np.cos(2 * x) - 7


# здесь объявляйте необходимые функции
def model(x, w):  # модель
    return w[0] + w[1] * x + w[2] * x ** 2 + w[3] * x ** 3 + w[4] * x ** 4

def loss(x, y, w):  # MSE
    return (model(x, w) - y) ** 2

def gradient(x, y, w):  # градиент
    x_vec = np.array([1, x, x ** 2, x ** 3, x ** 4])
    error = model(x, w) - func(x)
    return 2 * error * x_vec

coord_x = np.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = len(coord_x)	# количество значений функций (точек)
eta = np.array([0.01, 1e-3, 1e-4, 1e-5, 1e-6]) # шаг обучения для каждого параметра w0, w1, w2, w3, w4
w = np.array([0., 0., 0., 0., 0.]) # начальные значения параметров модели
N = 500 # число итераций алгоритма SGD
lm = 0.02 # значение параметра лямбда для вычисления скользящего экспоненциального среднего

Qe = 0.0 # начальное значение среднего эмпирического риска
np.random.seed(0) # генерация одинаковых последовательностей псевдослучайных чисел

# здесь продолжайте программу
for _ in range(N):
    k = np.random.randint(0, sz - 1)
    xk, yk = coord_x[k], coord_y[k]
    
    grad = gradient(xk, yk, w)
    w = w - eta * grad
    
    Lk = loss(xk, yk, w)
    Qe = lm * Lk + (1 - lm) * Qe

predictions = model(coord_x, w)
losses = (predictions - coord_y) ** 2  # MSE
Q = np.mean(losses)
