import torch
import torch.utils.data as data


class FuncDatasset(data.Dataset):
    def __init__(self):
        coord_x = torch.arange(-4, 4, 0.01)
        self.data = coord_x
        self.target = coord_x ** 2 + 0.5 * coord_x - torch.sin(5 * coord_x)
        self.length = coord_x.size(0)
        
    def __getitem__(self, indx):
        return self.data[indx], self.target[indx]
    
    def __len__(self):
        return self.length


ds = FuncDatasset()
d_train, d_val = data.random_split(ds, [0.8, 0.2])

train_data = data.DataLoader(d_train, batch_size=16, shuffle=True)
train_data_val = data.DataLoader(d_val, batch_size=100, shuffle=False)
