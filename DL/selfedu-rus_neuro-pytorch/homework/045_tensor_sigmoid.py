import torch


# все эти переменные в программе не менять
W = torch.rand(3) * 10 - 5
bias = torch.rand(1) * 100 - 50

batch_size = 8 # размер мини-батча
X = torch.empty(batch_size, 3).normal_(mean=1.0, std=4.0)

predict = (X @ W + bias).sigmoid()
