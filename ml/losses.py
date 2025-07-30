# сигмоидная
def loss(w, x, y):
    M = np.dot(w, x) * y
    return 2 / (1 + np.exp(M))

# MSE
def loss(x, y, w):
    return (model(x, w) - y) ** 2

# логарифмическая
def loss(w, x, y):
    M = np.dot(w, x) * y
    return np.log2(1 + np.exp(-M))

# экспоненциальная
def loss(w, x, y):
    M = np.dot(w, x) * y
    return np.exp(-M)

