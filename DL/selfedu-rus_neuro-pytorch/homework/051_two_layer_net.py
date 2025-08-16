import torch


def act_sigma(x):
    """
    Реализация функции активации для нейронов скрытого слоя.
    x - тензор [x1, x2]
    Функция должна возвращать тензор типа torch.float32 той же размерности, что и входной тензор x.
    """
    return x ** 2


def act_u(x):
    """
    Реализация функции активации для нейронов выходного слоя.
    x - тензор [x1]
    Функция должна возвращать тензор типа torch.float32 той же размерности, что и входной тензор x.
    """
    return x


# тензор X в программе не менять
batch_size = 16 # количество входных данных
X = torch.tensor(list(map(float, input().split())), dtype=torch.float32).view(batch_size, 2)

W1 = torch.tensor([(1, 0), (1, 0.5)], dtype=torch.float32)
bias1 = torch.tensor([0, 0], dtype=torch.float32)

W2 = torch.tensor([3, -2], dtype=torch.float32)
bias2 = torch.tensor([7.8], dtype=torch.float32)

h = torch.matmul(X, W1.transpose(1, 0) + bias1)  # h = torch.matmul(X, W1.T) + bias1)
h = act_sigma(h)

predict = h @ W2 + bias2
