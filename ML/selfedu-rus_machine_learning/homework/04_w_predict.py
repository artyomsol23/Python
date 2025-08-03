import numpy as np

x_test = [(5, -3), (-3, 8), (3, 6), (0, 0), (5, 3), (-3, -1), (-3, 3)]

# здесь продолжайте программу
w = (-33, 9, 13)

predict = [int(np.sign(w[0] + w[1] * x[0] + w[2] * x[1])) for x in x_test]
