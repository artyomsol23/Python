import torch
import matplotlib.pyplot as plt


N = 2
b = 0.5

def act(x: float):
    return 0 if x <= 0 else 1


def get_blue_points(_N: int):
    N = 2 * _N
    x = torch.rand(N)
    y = torch.rand(N)

    mask = (y > -x + 1.5) | (y < -x + 0.5)
    x, y = x[mask], y[mask]

    while len(x) < N:
        x_new = torch.rand(N)
        y_new = torch.rand(N)
        mask_new = (y_new > -x_new + 1.5) | (y_new < -x_new + 0.5)
        x = torch.cat([x, x_new[mask_new]])
        y = torch.cat([y, y_new[mask_new]])

    return torch.vstack([x[:N], y[:N], torch.ones(N)]).mT


def get_red_points(_N: int):
    N = 2 * _N
    x = torch.rand(N)
    y = torch.rand(N)

    mask = (y <= -x + 1.5) & (y >= -x + 0.5)
    x, y = x[mask], y[mask]

    while len(x) < N:
        x_new = torch.rand(N)
        y_new = torch.rand(N)
        mask_new = (y_new <= -x_new + 1.5) & (y_new >= -x_new + 0.5)
        x = torch.cat([x, x_new[mask_new]])
        y = torch.cat([y, y_new[mask_new]])

    return torch.vstack([x[:N], y[:N], torch.ones(N)]).mT


C1 = get_blue_points(N)
C2 = get_red_points(N * 2)

w1 = -1
w2 = -w1
w3 = -b * w2

w_hidden = torch.FloatTensor(
    [
        [1, 1, -1.5],
        [1, 1, -0.5],
    ],
)
w = torch.FloatTensor([w1, w2, w3])

def class_name(y: float, i: int, x: torch.Tensor):
    if y > 0:
        print(f"Класс C2: #{i+1}", x)
    else:
        print(f"Класс C1: #{i+1}", x)


def neuro_engine(x: torch.Tensor):
    z_hidden = torch.matmul(w_hidden, x)
    u_hidden = torch.FloatTensor([act(z) for z in z_hidden] + [1])

    z = torch.dot(w, u_hidden)
    return act(z)


def C1_test():
    for i in range(len(C1)):
        x = C1[i]
        y = neuro_engine(x)

        class_name(y, i, x)


def C2_test():
    for i in range(len(C2)):
        x = C2[i]
        y = neuro_engine(x)

        class_name(y, i, x)


C1_test()
C2_test()

plt.scatter(C1[:, 0], C1[:, 1], s=10, c="blue")
plt.scatter(C2[:, 0], C2[:, 1], s=10, c="red")

x_line = torch.linspace(0, 1, 100)
y1_line = -x_line + 1.5
y2_line = -x_line + 0.5

plt.plot(x_line, y1_line, label="y = -x + 1.5")
plt.plot(x_line, y2_line, label="y = -x + 0.5")

plt.axhline(0, color="grey", linewidth=0.5)
plt.axvline(0, color="grey", linewidth=0.5)

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.grid()
plt.show()
