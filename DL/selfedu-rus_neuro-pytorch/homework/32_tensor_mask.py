import torch


lst = list(map(float, input().split())) # список lst в программе не менять
tr = torch.tensor(lst, dtype=torch.float32)

t_mask = torch.ones(16, dtype=torch.int8)
t_mask[1::2] = torch.empty(8, dtype=torch.int8).fill_(-1)

tr[:16] = tr[:16] * t_mask.float()

print(*map(lambda _x: f"{_x.item():.1f}", tr))
