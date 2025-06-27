def factorial_2(n):  # Индуктивный (итеративный) вариант
    result = 1
    for i in range(1, n + 1):
        result *= i  # На каждом шаге используем предыдущее значение
    return result

def factorial_recursive(n):  # Рекурсивный вариант
    return 1 if n == 0 else n * factorial(n - 1)   # Если число = 1, то остановка рекурсии (базовый случай)

print("Факториал 5:", factorial(5))  # 120
print("Факториал 5:", factorial_recursive(5))  # 120
