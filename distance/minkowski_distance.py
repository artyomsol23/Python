def minkowski_distance(a: np.array, b: np.array, p=2) -> float:  # k-NN с метрикой Минковского
    return np.sum(np.abs(a - b) ** p) ** (1 / p)                 # по умолчанию Евклидово расстояние
