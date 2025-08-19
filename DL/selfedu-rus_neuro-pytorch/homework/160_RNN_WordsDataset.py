import torch
import torch.nn as nn
import torch.utils.data as data


class WordsDataset(data.Dataset):
    # инициализатор класса
    def __init__(self, batch_size=8):
        # здесь код, относящийся к инициализатору
        self.batch_size = batch_size
        self.words_lst = [(x0, 0) for x0 in _global_words_0] + [(x1, 1) for x1 in _global_words_1]
        self.words_lst.sort(key=lambda x: len(x[0]))
        self.dataset_len = len(self.words_lst)
        text = "".join(_global_words_0 + _global_words_1).lower()
        self.alphabet = set(text)
        self.int_to_alpha = dict(enumerate(sorted(self.alphabet)))
        self.alpha_to_int = {b: a for a, b in self.int_to_alpha.items()}
        self.num_characters = len(self.alphabet)
        self.onehots = torch.eye(self.num_characters + 1, self.num_characters)

    # формирование и возвращение батча данных по индексу item
    def __getitem__(self, idx):
        # здесь код, относящийся к __getitem__
        idx *= self.batch_size
        idx_last = idx + self.batch_size
        
        if idx_last > self.dataset_len:
            idx_last = self.dataset_len

        max_length = len(self.words_lst[idx_last - 1][0])

        d = [[self.alpha_to_int[x] for x in w[0]] + [-1] * (max_length - len(w[0]))
             for w in self.words_lst[idx: idx_last]
            ]
        t = torch.FloatTensor([w[1] for w in self.words_lst[idx: idx_last]])

        data = torch.zeros(len(d), max_length, self.num_characters)
        
        for i, x in enumerate(d):
            data[i, :, :] = self.onehots[x]

        return data, t
        
    # возврат размер обучающей выборки в батчах
    def __len__(self):
        # здесь код, относящийся к __len__
        last = 0 if self.dataset_len % self.batch_size == 0 else 1
        return self.dataset_len // self.batch_size + last


# здесь продолжайте программу
d_train = WordsDataset(batch_size=8)

train_data = data.DataLoader(d_train, batch_size=1, shuffle=True)
