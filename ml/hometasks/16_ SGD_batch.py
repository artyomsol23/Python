import numpy as np

# исходная функция, которую нужно аппроксимировать моделью a(x)
def func(x):
    return 0.5 * x + 0.2 * x ** 2 - 0.05 * x ** 3 + 0.2 * np.sin(4 * x) - 2.5


# здесь объявляйте необходимые функции
def create_feature_matrix(x):  # для создания матрицы признаков
    return np.column_stack([np.ones_like(x), x, x ** 2, x ** 3])

def predict(X, w):  # для вычисления предсказания модели
    return X.dot(w)

def compute_Qk(X_batch, y_batch, w):  # для вычисления усеченного эмпирического риска
    residuals = predict(X_batch, w) - y_batch
    return np.mean(residuals ** 2)

def compute_gradient(X_batch, y_batch, w):  # для вычисления градиента
    residuals = predict(X_batch, w) - y_batch
    gradient = 2 * np.mean(residuals.reshape(-1, 1) * X_batch, axis=0)
    return gradient


coord_x = np.arange(-4.0, 6.0, 0.1) # значения по оси абсцисс [-4; 6] с шагом 0.1
coord_y = func(coord_x) # значения функции по оси ординат

sz = len(coord_x)	# количество значений функций (точек)
eta = np.array([0.1, 0.01, 0.001, 0.0001]) # шаг обучения для каждого параметра w0, w1, w2, w3
w = np.array([0., 0., 0., 0.]) # начальные значения параметров модели
N = 500 # число итераций алгоритма SGD
lm = 0.02 # значение параметра лямбда для вычисления скользящего экспоненциального среднего
batch_size = 50 # размер мини-батча (величина K = 50)

Qe = 0.0 # начальное значение среднего эмпирического риска
np.random.seed(0) # генерация одинаковых последовательностей псевдослучайных чисел

X = create_feature_matrix(coord_x)
y = coord_y

for _ in range(N):
    k = np.random.randint(0, sz - batch_size)
    X_batch = X[k:k + batch_size]
    y_batch = y[k:k + batch_size]
    
    gradient = compute_gradient(X_batch, y_batch, w)
    w -= eta * gradient
    
    Qk = compute_Qk(X_batch, y_batch, w)
    Qe = lm * Qk + (1 - lm) * Qe

Q = compute_Qk(X, y, w)
