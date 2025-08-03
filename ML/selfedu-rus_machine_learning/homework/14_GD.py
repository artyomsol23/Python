import numpy as np

# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.1 * x**2 - np.sin(x) + 5.


# здесь объявляйте необходимые функции
def compute_gradient(w, X, y):
    n = len(X)
    gradient = np.zeros_like(w)
    
    for i in range(n):
        x = X[i]
        si = np.array([1, x, x ** 2, x ** 3])
        error = np.dot(w, si) - y[i]
        
        gradient += 2 * error * si
        
    gradient /= n
    
    return gradient

coord_x = np.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = len(coord_x)	# количество значений функций (точек)
eta = np.array([0.1, 0.01, 0.001, 0.0001]) # шаг обучения для каждого параметра w0, w1, w2, w3
w = np.array([0., 0., 0., 0.]) # начальные значения параметров модели
N = 200 # число итераций градиентного алгоритма

# здесь продолжайте программу
for _ in range(N):
    gradient = compute_gradient(w, coord_x, coord_y)
    
    w -= eta * gradient  # поиск весов

Q = 0.0

for i in range(sz):
    x = coord_x[i]
    si = np.array([1, x, x ** 2, x ** 3])  # вектор признаков
    
    ax = np.dot(w, si)                     # предсказание модели
    Q += (ax - coord_y[i]) ** 2            # квадрат ошибки

Q /= sz  # эмпирический риск
