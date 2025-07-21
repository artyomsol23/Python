import numpy as np

def gini(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    proportions = np.bincount(y) / len(y)
    return 1 - np.sum(proportions ** 2)
