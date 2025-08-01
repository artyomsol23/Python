import numpy as np

TP = [57, 48, 60, 55]
TN = [32, 35, 28, 41]
FP = [13, 15, 12, 11]
FN = [7, 12, 11, 8]

precisions = [TP / (TP + FP) for TP, FP in zip(TP, FP)]
recalls = [TP / (TP + FN) for TP, FN in zip(TP, FN)]

precision = np.mean(precisions)
recall = np.mean(recalls)
