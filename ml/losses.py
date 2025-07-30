import numpy as np

# MAE базовая
def mae_loss(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred)) + 1e-10

# MAE классическая для регрессии
def mae_loss(y_true, y_pred):
    return np.mean(np.abs(y_pred - y_true)) + 1e-10

# MAE для векторов
def mae_loss(x, y, w):
    y_pred = np.dot(w, x)  # w.T @ x, если w и x — векторы-столбцы
    return np.mean(np.abs(y_pred - y)) + 1e-10

# MAE для матрицы X, вектора y
def mae_loss(X, y, w):
    y_pred = np.dot(X, w)
    return np.mean(np.abs(y_pred - y)) + 1e-10

# MAE для нелинейной модели
def mae_loss(x, y, w):
    return np.mean(np.abs(model(x, w) - y)) + 1e-10

# MAE + L1 регуляризация
def mae_l1_loss(y_true, y_pred, w, alpha=0.01):
    mae = np.mean(np.abs(y_true - y_pred)) + 1e-10
    l1 = alpha * np.sum(np.abs(w))
    return mae + l1

# MAE + L2 регуляризация
def mae_l2_loss(y_true, y_pred, w, alpha=0.01):
    mae = np.mean(np.abs(y_true - y_pred)) + 1e-10
    l2 = alpha * np.sum(w ** 2)
    return mae + l2

# MSE базовая
def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2) + 1e-10

# MSE классическая для регрессии (между истинными значениями и предсказаниями)
def mse_loss(y_true, y_pred):
    return np.mean((y_pred - y_true) ** 2) + 1e-10

# MSE для векторов
def mse_loss(x, y, w):
    y_pred = np.dot(w, x)  # w.T @ x, если w и x — векторы-столбцы
    return np.mean((y_pred - y) ** 2) + 1e-10

# MSE для матрицы X, вектора y
def mse_loss(X, y, w):
    y_pred = np.dot(X, w)
    return np.mean((y_pred - y) ** 2) + 1e-10

# MSE для нелинейной модели
def mse_loss(x, y, w):
    return np.mean((model(x, w) - y) ** 2) + 1e-10

# MSE + L1
def mse_l1_loss(y_true, y_pred, w, alpha=0.01):
    mse = np.mean((y_true - y_pred) ** 2) + 1e-10
    l1 = alpha * np.sum(np.abs(weights))
    return mse + l1

# MSE + L2
def mse_l2_loss(y_true, y_pred, w, alpha=0.01):
    mse = np.mean((y_true - y_pred) ** 2) + 1e-10
    l2 = alpha * np.sum(w ** 2)
    return mse + l2

# MSE для батча данных
def mse_batch_loss(y_true, y_pred, batch_size):
    errors = (y_true - y_pred) ** 2
    if batch_size is None:
        batch_size = len(y_true)
    return np.sum(errors) / batch_size + 1e-10

# сигмоидная
def sig_loss(w, x, y):
    M = np.dot(w, x) * y
    return 2 / (1 + np.exp(M))

# логарифмическая
def log_loss(w, x, y):
    M = np.dot(w, x) * y
    return np.log2(1 + np.exp(-M))

# экспоненциальная
def exp_loss(w, x, y):
    M = np.dot(w, x) * y
    return np.exp(-M)
