def factorial_recursive(n: int):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
