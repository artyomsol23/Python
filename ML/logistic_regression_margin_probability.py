import numpy as np

def logistic_regression_margin_probability(w: np.ndarray, x: np.ndarray) -> tuple:
    margin = np.dot(w, x)
    probability = 1 / (1 + np.exp(-margin))
    
    return round(margin, 2), round(probability, 2)
  
