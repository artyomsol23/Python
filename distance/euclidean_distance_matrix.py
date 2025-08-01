import numpy as np

def euclidean_distance_matrix(X, Y):
    X_sq = np.sum(X ** 2, axis=1, keepdims=True)
    Y_sq = np.sum(Y ** 2, axis=1)
    XY = np.dot(X, Y.T)
    return np.sqrt(X_sq + Y_sq - 2 * XY)
