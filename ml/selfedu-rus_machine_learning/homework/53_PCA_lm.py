import numpy as np

np.random.seed(0)

n_total = 1000 # число образов выборки
n_features = 200 # число признаков

table = np.zeros(shape=(n_total, n_features))

for _ in range(100):
    i, j = np.random.randint(0, n_total), np.random.randint(0, n_features)
    table[i, j] = np.random.randint(1, 10)

# матрицу table не менять

# здесь продолжайте программу
F = table.T @ table / len(table)
L, W = np.linalg.eig(F)

WW = sorted(zip(L, W), key=lambda lx: lx[0], reverse=True)
WW = np.array([w[1] for w in WW])

data_x = table @ WW.T

lm = 0.01

data_x = data_x[:, L >= lm]  # lm > 0.01
