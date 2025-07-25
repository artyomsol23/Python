import numpy as np

x1, y1, x2, y2 =  # координаты точек

x = np.array([[x1, 1], [x2, 1]])
y = np.array([y1, y2])
k, b = np.linalg.solve(x, y)
w0, w1, w2 = -b, -k, 1

w = np.array([w0, w1, w2])
