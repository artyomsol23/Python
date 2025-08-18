import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# сюда копируйте класс WordsDataset, созданный на предыдущем занятии
class WordsDataset(data.Dataset):
    def __init__(self, navec_emb, prev_words=4):
        self.prev_words = prev_words
        self.navec_emb = navec_emb
        self.lines = _global_var_text
        self.vocab = set((' '.join(self.lines)).lower().split())
        self.vocab_size = len(self.vocab)

        data = []
        targets = []

        for target in self.lines:
            words = target.lower().split()
            
            for item in range(len(words) - self.prev_words):
                data.append([self.navec_emb[words[x]].tolist() for x in range(item, item + self.prev_words)])
                targets.append(self.navec_emb.vocab[words[item + self.prev_words]])

        self.data = torch.tensor(data)
        self.targets = torch.tensor(targets)
        self.length = len(data)

    def __getitem__(self, idx):
        return self.data[idx], self.targets[idx]

    def __len__(self):
        return self.length


# здесь объявляйте класс модели
class WordsRNN(nn.Module):
    def __init__(self, input_size, output_size, hidden_size=16):
        super().__init__()
        self.hidden_size = hidden_size
        self.in_features = input_size
        self.out_features = output_size
        self.rnn = nn.RNN(self.in_features, self.hidden_size, batch_first=True)
        self.out = nn.Linear(self.hidden_size, self.out_features)

    def forward(self, x):
        x, h = self.rnn(x)
        return self.out(h)


# сюда копируйте объекты d_train и train_data, созданные на предыдущем занятии
d_train = WordsDataset(global_navec)
train_data = data.DataLoader(d_train, batch_size=8, shuffle=True)

# создайте объект модели для прогноза слов
model = WordsRNN(100, len(global_navec.vocab))

# создайте оптимизатор Adam с шагом обучения 0.01 и параметром weight_decay=0.0001
optim = optim.Adam(params=model.parameters(), lr=0.01, weight_decay=0.0001)
# создайте функцию потерь кросс-энтропию для задачи многоклассовой классификации
loss_func = nn.CrossEntropyLoss()

# переведите модель в режим обучения
model.train()

# число эпох обучения (в реальности нужно от 100 и более)
epochs = 1

for _ in range(epochs):
    # с помощью цикла for переберите батчи из объекта train_data
    for x, y in train_data:
        predict = model(x).squeeze(0)        # вычислите прогноз модели для x_train
        loss = loss_func(predict, y.long())  # вычислите потери для predict и y_train

        # выполните один шаг обучения (градиентного спуска)
        optim.zero_grad()
        loss.backward()
        optim.step()

# переведите модель в режим эксплуатации
model.eval()

predict = "Такими были первые нейронные сети предложенные".lower().split()
int_to_word = dict(enumerate((global_navec.vocab)))
total = 10  # число прогнозируемых слов (дополнительно к начальной фразе)

# выполните прогноз следующих total слов
for _ in range(total):
    _data = torch.tensor([d_train.navec_emb[predict[-x]].tolist() for x in range(d_train.prev_words, 0, -1)])
    
    with torch.no_grad():
        next_word = model(_data.unsqueeze(0)).squeeze(0)
    
    idx = torch.argmax(next_word, dim=1)
    predict.append(int_to_word[idx.item()])

predict = " ".join(predict)

# выведите полученную строку на экран
print(predict)
