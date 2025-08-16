import torch


# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.1 * x ** 2 - torch.sin(x) + 5.


# здесь объявляйте необходимые функции
def model(w, x):  # ф-ия, возвращающая значения в точке x
    return w[0] + w[1] * x + w[2] * x ** 2 + w[3] * x ** 3


def loss(w, x, y):  # ф-ция потерь
    return (model(w, x) - y) ** 2


def dL(w, x, y):  # производная ф-ции потерь
    return 2 * (model(w, x) - y) * torch.tensor([1, x, x ** 2, x ** 3], dtype=torch.float32)


coord_x = torch.arange(-5.0, 5.0, 0.1) # значения по оси абсцисс [-5; 5] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = coord_x.size(0)	# количество значений функций (точек)
eta = torch.tensor([0.1, 0.01, 0.001, 0.0001]) # шаг обучения для каждого параметра w0, w1, w2, w3
w = torch.zeros(4, dtype=torch.float32) # начальные значения параметров модели
N = 200 # число итераций градиентного алгоритма

# здесь продолжайте программу
for _ in range(N):
    grad = 0
    
    for i in range(sz):
        grad += dL(w, coord_x[i], coord_y[i])
    
    w -= eta * grad / sz

Q = torch.mean(loss(w, coord_x, coord_y)).item()
