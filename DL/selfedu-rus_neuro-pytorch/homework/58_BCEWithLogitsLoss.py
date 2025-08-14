import torch


# значения predict, target не менять
batch_size = 8
target = torch.randint(0, 2, (batch_size, 1), dtype=torch.float32) # целевые значения
predict = torch.empty(batch_size, 1).normal_(0, 2.0) # прогнозные значения

loss = torch.nn.BCEWithLogitsLoss()

Q = loss(predict, target).item()  # ф-ия sigmoid применяется автоматически в BCEWithLogitsLoss

p_sigm = predict.sigmoid()  # torch.nn.functional.sigmoid(predict)
Q_bce = -torch.mean(target * torch.log(p_sigm) + (1 - target) * torch.log(1 - p_sigm)).item()
