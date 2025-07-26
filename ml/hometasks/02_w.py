import numpy as np

np.random.seed(0) # псевдослучайные числа образуют одну и ту же последовательность (при каждом запуске)
x = np.arange(-1.0, 1.0, 0.1) # аргумент [-1; 1] с шагом 0,1


model_a = lambda xx, ww: (ww[0] + ww[1] * xx) # модель
Y = -5.2 + 0.7 * x + np.random.normal(0, 0.1, len(x)) # вектор целевых значений

# здесь продолжайте программу
X = np.column_stack([np.ones(len(x)), x])
X_T = X.transpose()
X_T_X = X_T @ X
X_T_X_inv = np.linalg.inv(X_T_X)
X_T_Y = X_T @ Y
w = X_T_X_inv @ X_T_Y
