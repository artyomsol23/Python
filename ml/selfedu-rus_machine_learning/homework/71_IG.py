import numpy as np

np.random.seed(0)
X = np.random.randint(0, 2, size=200)

# здесь продолжайте программу
t = 150
X_left, X_right = X[:t], X[t:]

P0, P1 = np.mean(X == 0), np.mean(X == 1)
P0_left, P1_left = np.mean(X_left == 0), np.mean(X_left == 1)
P0_right, P1_right = np.mean(X_right == 0), np.mean(X_right == 1)

# impurity по критерию Джини
S0 = 1 - (P0 ** 2 + P1 ** 2)
S1 = 1 - (P0_left ** 2 + P1_left ** 2)
S2 = 1 - (P0_right ** 2 + P1_right ** 2)

IG = S0 - ((len(X_left) / len(X)) * S1 + (len(X_right) / len(X)) * S2)  # информационный выигрыш
