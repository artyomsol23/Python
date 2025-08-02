import numpy as np

x = np.arange(-2, 3, 0.1)
y = -x + 0.2 * x ** 2 - 0.5 * np.sin(4*x) + np.cos(2*x)

# здесь продолжайте программу
IG = -1
th = 0.0
N0 = len(y)
b = np.mean(y)

HR = np.sum((b - y) ** 2)

for t in x:
    left_i = np.where(x < t)[0]
    right_i = np.where(x >= t)[0]
    
    y1, y2 = y[left_i], y[right_i]
    
    if len(y1) == 0 or len(y2) == 0:
        continue
    
    b1, b2 = np.mean(y1), np.mean(y2)
    N1, N2 = len(y1), len(y2)
    
    # MSE (impurity)
    HR1 = np.sum((b1 - y1) ** 2)
    HR2 = np.sum((b2 - y2) ** 2)
    
    IG_new = HR - (((N1 / N0) * HR1) + ((N2 / N0) * HR2))
    
    if IG_new > IG:
        IG = IG_new
        th = t
