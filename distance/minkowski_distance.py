# k-NN с метрикой Минковского
def minkowski_distance(a: np.array, b: np.array, p=2) -> float:  # по умолчанию Евклидово расстояние
    return np.sum(np.abs(a - b) ** p) ** (1 / p)                 # np.sum(np.abs(a - b) ** p, axis=-1) ** (1 / p), если
                                                                 # необходимо суммирование по последней оси (признакам)
