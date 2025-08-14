import torch


tr = torch.tensor([[-10, -8], [-6, -4], [-2, 0], [2, 4], [6, 8]], dtype=torch.int32)
tr_t = tr.transpose(0, 1)  # tr.t() / tr.permute(1, 0)
