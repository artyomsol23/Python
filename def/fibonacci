def fibonacci_recursive(n):  # Индуктивный (итеративный) вариант
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_recursive(n):  # Рекурсивный вариант
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("5-е число Фибоначчи:", fibonacci(5))  # 5
print("5-е число Фибоначчи:", fibonacci_recursive(5))  # 5
