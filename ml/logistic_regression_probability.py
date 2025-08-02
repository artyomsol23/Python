import numpy as np

def logistic_regression_probability(w: np.ndarray, x: np.ndarray) -> float:
    a_x = np.dot(w, x)                   # линейная комбинация w^T * x
    probability = 1 / (1 + np.exp(a_x))  # cигмоидная функция
    
    return round(probability, 2)
