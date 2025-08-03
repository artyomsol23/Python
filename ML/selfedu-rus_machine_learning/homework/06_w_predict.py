import numpy as np

x_test = [(9, 6), (2, 4), (-3, -1), (3, -2), (-3, 6), (7, -3), (6, 2)]

# здесь продолжайте программу
w = (14, -7, 5)

predict = [int(np.sign(w[0] + w[1] * x[0] + w[2] * x[1])) for x in x_test]
