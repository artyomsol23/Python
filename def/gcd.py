def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print("НОД чисел 54 и 24:", gcd(54, 24))  # 6
