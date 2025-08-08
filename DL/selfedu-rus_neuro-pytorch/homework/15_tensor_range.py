import torch


t_indx = torch.arange(1, 65, 1, dtype=torch.int64).view(2, 32)
# t_indx = torch.tensor(range(1, 65), dtype=torch.int64).view(2, 32)
# t_indx = torch.LongTensor(list(range(1, 65))).view(2, 32)
