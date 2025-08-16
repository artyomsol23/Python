import torch


m1 = torch.arange(1, 13, dtype=torch.int16).reshape(3, 4)
m2 = torch.arange(10, 130, 10, dtype=torch.int16).reshape(3, 4)
m3 = torch.arange(-1, -13, -1, dtype=torch.int16).reshape(3, 4)

tr3d = torch.stack([m1, m2, m3])

tm = tr3d[1]
