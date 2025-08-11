import torch

def act_sigma(x):
    """
    Реализация функции активации для нейронов скрытого слоя.
    x - тензор [x1, x2]
    Функция должна возвращать тензор типа torch.float32 той же размерности, что и входной тензор x.
    """
    return torch.sin(x)


def act_u(x):
    """
    Реализация функции активации для нейронов выходного слоя.
    x - тензор [x1]
    Функция должна возвращать тензор типа torch.float32 той же размерности, что и входной тензор x.
    """
    return torch.sign(x - 0.5)


# тензор X в программе не менять
batch_size = 16 # количество входных данных
X = torch.tensor(list(map(float, input().split())), dtype=torch.float32).view(batch_size, 2)

W1 = torch.tensor([(0.5 * torch.pi, 0.5 * torch.pi), (0, 0.1)], dtype=torch.float32)
bias1 = torch.tensor([1.5, -1.5 * torch.pi], dtype=torch.float32)

W2 = torch.tensor([2, -3.5], dtype=torch.float32)
bias2 = torch.tensor([0], dtype=torch.float32)

h = torch.matmul(X, W1.transpose(1, 0)) + bias1  # h = torch.matmul(X, W1.T + bias1
h = act_sigma(h)

predict = act_u(h @ W2 + bias2)
