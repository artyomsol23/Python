import torch
import torch.utils.data as data
import torch.nn as nn
import torch.optim as optim


class IrisDataset(data.Dataset):
    def __init__(self):
        self.data = _global_var_data_x # тензор размерностью (150, 4), тип float32
        self.target = _global_var_target # тензор размерностью (150, ), тип int64 (long)
        self.length = len(self.data) # размер выборки
        self.categories = ['setosa' 'versicolor' 'virginica'] # названия классов
        self.features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

    def __getitem__(self, item):
        # возврат образа по индексу item в виде кортежа: (данные, целевое значение)
        return self.data[item], self.target[item]
        
    def __len__(self):
        # возврат размера выборки
        return self.length


class IrisClassModel(nn.Module):
    def __init__(self, in_features=4, out_features=3):
        super().__init__()
        # модель нейронной сети из двух полносвязных слоев:
        # 1-й слой: число входов in_features, число нейронов 16
        self.layer1 = nn.Linear(in_features, 16)
        # 2-й слой: число нейронов out_features
        self.layer2 = nn.Linear(16, out_features)

    def forward(self, x):
        # тензор x пропускается через 1-й слой
        x = self.layer1(x)
        # через функцию активации torch.relu()
        x = torch.relu(x)
        # через второй слой
        x = self.layer2(x)
        
        # полученный (вычисленный) тензор возвращается
        return x


torch.manual_seed(11)

# создать модель IrisClassModel с числом входов 4 и числом выходов 3
model = IrisClassModel()
# перевести модель в режим обучения
model.train()

# размер батча
batch = 8
# создать объект класса IrisDataset
d_train = IrisDataset()
# создать объект класса DataLoader с размером пакетов batch_size и перемешиванием образов выборки
train_data = data.DataLoader(d_train, batch, shuffle=True)

# создать оптимизатор Adam для обучения модели с шагом обучения 0.01
optimizer = optim.Adam(params=model.parameters(), lr=0.01)
# создать функцию потерь с помощью класса CrossEntropyLoss (используется при многоклассовой классификации)
loss_func = torch.nn.CrossEntropyLoss()

epochs = 10 # число эпох обучения

for _ in range(epochs): # итерации по эпохам
    for x, y in train_data:
        # вычислить прогноз модели для данных x
        predict = model(x)
        # вычислить значение функции потерь
        loss = loss_func(predict, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# перевести модель в режим эксплуатации
model.eval()
# выполнить прогноз модели по всем данным выборки
predict = model(d_train.data)
predict = torch.argmax(predict, dim=1)

# вычислить долю верных классификаций (сохранить, как вещественное число, а не тензор)
Q = torch.mean((predict == d_train.target).float()).item()
