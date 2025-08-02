import numpy as np

def gini(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)  # для любого заданного класса
    p = counts / len(y)
    return 1 - np.sum(p ** 2)
  
