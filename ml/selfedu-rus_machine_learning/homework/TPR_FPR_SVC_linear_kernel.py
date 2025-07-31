import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

np.random.seed(0)

# исходные параметры распределений классов
r1 = 0.2
D1 = 3.0
mean1 = [2, -2]
V1 = [[D1, D1 * r1], [D1 * r1, D1]]

r2 = 0.5
D2 = 2.0
mean2 = [-1, -1]
V2 = [[D2, D2 * r2], [D2 * r2, D2]]

# моделирование обучающей выборки
N1 = 1000
N2 = 1000
x1 = np.random.multivariate_normal(mean1, V1, N1).T
x2 = np.random.multivariate_normal(mean2, V2, N2).T

data_x = np.hstack([x1, x2]).T
data_y = np.hstack([np.ones(N1) * -1, np.ones(N2)])

x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, random_state=123,test_size=0.5, shuffle=True)

# здесь продолжайте программу
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

w1, w2 = clf.coef_[0]
w0 = clf.intercept_[0]
w = (w0, w1, w2)

t = 2

predict = np.sign(np.dot(x_test, [w1, w2]) + w0 - t)

# Вариант 2
# decision_values = clf.decision_function(x_test)
# predict = np.where(decision_values >= t, 1, -1)

TP = np.sum((predict == 1) & (y_test == 1))
FP = np.sum((predict == 1) & (y_test == -1))
TN = np.sum((predict == -1) & (y_test == -1))
FN = np.sum((predict == -1) & (y_test == 1))

TPR = TP / (TP + FN) if (TP + FN) > 0 else 0.0
FPR = FP / (FP + TN) if (FP + TN) > 0 else 0.0
