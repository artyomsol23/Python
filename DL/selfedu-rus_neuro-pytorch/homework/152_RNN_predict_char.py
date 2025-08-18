import torch
import torch.nn as nn
import torch.utils.data as data
import torch.optim as optim


# сюда копируйте класс CharsDataset из предыдущего подвига
class CharsDataset(data.Dataset):
    def __init__(self, prev_chars=7):
        self.prev_chars = prev_chars
        self.lines = _global_var_text
        self.alphabet = set(("".join(self.lines)).lower())
        self.int_to_alpha = dict(enumerate(sorted(self.alphabet)))
        self.alpha_to_int = {b: a for a, b in self.int_to_alpha.items()}
        self.num_characters = len(self.alphabet)
        self.onehots = torch.eye(self.num_characters)

        data = []
        targets = []

        for i, t in enumerate(self.lines):
            t = t.lower()
            
            for item in range(len(t) - self.prev_chars):
                data.append([self.alpha_to_int[t[x]] for x in range(item, item + self.prev_chars)])
                targets.append(self.alpha_to_int[t[item + self.prev_chars]])

        self.data = torch.tensor(data)
        self.targets = torch.tensor(targets)
        self.length = len(data)

    def __getitem__(self, indx):
        return self.onehots[self.data[idx]], self.targets[idx]

    def __len__(self):
        return self.length


# здесь объявляйте класс модели нейронной сети
class TextRNN(nn.Module):
    def __init__(self, input_size, output_size, hidden_size=32):
        super().__init__()
        self.hidden_size = hidden_size
        self.in_features = input_size
        self.out_features = output_size
        self.rnn = nn.RNN(self.in_features, self.hidden_size, batch_first=True)
        self.out = nn.Linear(self.hidden_size, self.out_features)

    def forward(self, x):
        x, h = self.rnn(x)
        return self.out(h)


# сюда копируйте объекты d_train и train_data
d_train = CharsDataset(prev_chars=10)
train_data = data.DataLoader(d_train, batch_size=8, shuffle=True)

# создайте объект модели
model = TextRNN(d_train.num_characters, d_train.num_characters)

# оптимизатор Adam с шагом обучения 0.01
optim = optim.Adam(params=model.parameters(), lr=0.01)
# функция потерь - CrossEntropyLoss
loss_func = nn.CrossEntropyLoss()

 
model.train()  # переведите модель в режим обучения

epochs = 1     # число эпох (это конечно, очень мало, в реальности нужно от 100 и более)

for _ in range(epochs):
    for x, y in train_data:
        predict = model(x).squeeze(0)        # вычислите прогноз модели для x_train
        loss = loss_func(predict, y.long())  # вычислите потери для predict и y_train

        # выполните один шаг обучения (градиентного спуска)
        optim.zero_grad()
        loss.backward()
        optim.step()

# переведите модель в режим эксплуатации
model.eval()

predict = "нейронная сеть ".lower() # начальная фраза
total = 20                          # число прогнозируемых символов (дополнительно к начальной фразе)

# выполните прогноз следующих total символов
for _ in range(total):
    _data = d_train.onehots[[d_train.alpha_to_int[predict[-x]] for x in range(d_train.prev_chars, 0, -1)]]
    
    with torch.no_grad():
        predict_char = model(_data.unsqueeze(0)).squeeze(0)
        
    indx = torch.argmax(predict_char, dim=1)
    predict += d_train.int_to_alpha[indx.item()]

# выведите полученную строку на экран
print(predict)
