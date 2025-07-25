import numpy as np

def line_coefficients(x1: float, y1: float, x2: float, y2: float) -> np.array:
    x = np.array([[x1, 1], [x2, 1]])
    y = np.array([y1, y2])
    k, b = np.linalg.solve(x, y)
    w0, w1, w2 = -b, -k, 1
    return np.array([w0, w1, w2])
  
