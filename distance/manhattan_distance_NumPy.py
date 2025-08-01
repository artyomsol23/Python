import numpy as np

def manhattan_distance(x1, x2) -> np.ndarray:
    return np.sum(np.abs(x1 - x2), axis=1)
