def func(x):
    return 0.5 * x + 0.2 * x ** 2 - 0.1 * x ** 3


def df(x):
    # здесь выражение производной функции f(x)
    return 0.5 + 0.4 * x - 0.3 * x ** 2


# здесь продолжайте программу
eta = 0.01
x = -4.0
N = 200

for _ in range(N):
    x -= eta * df(x)
  
