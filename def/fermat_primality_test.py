import random
import math

def fermat_primality_test(n: int, k: int = 5):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        
        if math.gcd(a, n) != 1:
            return False
        
        if pow(a, n - 1, n) != 1:
            return False

    return True
