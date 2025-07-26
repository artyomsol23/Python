import numpy as np
import math

def line_weights(x1: float, y1: float, x2: float, y2: float) -> np.array:
    w1 = y2 - y1
    w2 = x1 - x2
    w0 = x2 * y1 - x1 * y2

    # нормировка
    gcd_all = math.gcd(math.gcd(abs(int(w0)), math.gcd(abs(int(w1)), abs(int(w2))))
    if gcd_all > 1:
        w0 /= gcd_all
        w1 /= gcd_all
        w2 /= gcd_all

    return np.array([w0, w1, w2])
