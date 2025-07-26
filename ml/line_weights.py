import numpy as np

def line_weights(x1: float, y1: float, x2: float, y2: float) -> np.array:
    w1 = y2 - y1
    w2 = x1 - x2
    w0 = x2 * y1 - x1 * y2
    return np.array([w0, w1, w2])
