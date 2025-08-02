import numpy as np

def gini(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0      
    # Для преобразования {-1, 1} в {0, 1}:
    # y_transf = (y == 1)
    # p = np.bincount(y_transf) / len(y)
    p = np.bincount(y) / len(y)
    return 1 - np.sum(p ** 2)
