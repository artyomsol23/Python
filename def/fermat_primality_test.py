import random
import math

def fermat_primality_test(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if math.gcd(a, n) != 1:
            return False
        if pow(a, n - 1, n) != 1:
            return False
    return True  # Вероятно (!) простое

# Пример использования
print(fermat_primality_test(17))  # True (простое)
print(fermat_primality_test(561)) # True (561 — число Кармайкла!)
