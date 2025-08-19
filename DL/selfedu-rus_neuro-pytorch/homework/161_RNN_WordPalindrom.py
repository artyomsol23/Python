import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# сюда копируйте класс WordsDataset, созданный на предыдущем занятии
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


# здесь объявляйте класс модели
class WordPalindrom(nn.Module):
    def __init__(self, in_features):
        super().__init__()
        self.hidden_size = 16
        self.in_features = in_features
        self.rnn = nn.RNN(
            input_size=in_features,
            hidden_size=self.hidden_size,
            num_layers=1,
            nonlinearity='tanh',
            bias=True, 
            batch_first=True,
            dropout=0,
            bidirectional=True
        )
        self.out = nn.Linear(
            in_features=self.hidden_size * 2,
            out_features=1,
            bias=True
        )

    def forward(self, x):
        _, h = self.rnn(x)
        y = torch.cat([h[0], h[1]], dim=1)
        return self.out(y)


d_train = WordsDataset()
train_data = data.DataLoader(d_train, batch_size=1, shuffle=True)

# создание модели с числом входов, равным размеру словаря (размеру one-hot векторов)
d_train = WordsDataset(batch_size=8)
train_data = data.DataLoader(d_train, batch_size=1, shuffle=True)

model = WordPalindrom(d_train.num_characters)

# оптимизатор Adam с шагом обучения 0.01 и параметром weight_decay=0.001
optim = optim.Adam(params=model.parameters(), lr=0.01, weight_decay=0.001)
# бинарная кросс-энтропия BCEWithLogitsLoss
loss_func = nn.BCEWithLogitsLoss()

model.train()  # переведите модель в режим обучения

epochs = 2     # число эпох обучения (в реальности нужно от 100 и более)

for _ in range(epochs):
    for x, y in train_data:
        # вычислите прогноз модели для x_train
        predict = model(x.squeeze(0))
        # вычислите потери для predict и y_train
        loss = loss_func(predict, y.view(-1, 1))

        # выполните один шаг обучения (градиентного спуска)
        optim.zero_grad()
        loss.backward()
        optim.step()

model.eval()  # переведите модель в режим эксплуатации

Q = 0         # начальное значение доли верных классификаций


for x, y in train_data:
    with torch.no_grad():
        # вычислите прогноз модели для x_train
        p = model(x.squeeze(0))
        # вычислите долю верных классификаций для p и y_train
        Q += torch.mean((torch.sign(p.flatten()) == 2 * y.flatten() - 1).float())

Q /= len(d_train) # усреднение по всем батчам
