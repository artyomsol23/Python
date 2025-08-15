import torch
import torch.nn as nn
import torch.utils.data as data


# здесь продолжайте программу
class FuncDataset(data.Dataset):
    def __init__(self):
        self.coord_x = torch.arange(-5, 5, 0.1)
        self.func = 2 * torch.exp(-self.coord_x / 2) + 0.2 * torch.sin(self.coord_x / 10) - 5
        self.length = len(self.coord_x)
        
    def __getitem__(self, indx):
        return self.coord_x[indx], self.func[indx]
    
    def __len__(self):
        return self.length
    

d_train = FuncDataset()
x13, y13 = d_train[13]
total = len(d_train)
