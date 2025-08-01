import numpy as np

TP = [45, 37, 51, 47]
TN = [36, 37, 29, 28]
FP = [18, 21, 15, 17]
FN = [8, 11, 9, 5]

sum_TP = np.sum(TP)
sum_FP = np.sum(FP)
sum_FN = np.sum(FN)

precision = sum_TP / (sum_TP + sum_FP)
recall = sum_TP / (sum_TP + sum_FN)
