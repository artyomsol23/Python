def matrix_power(A, power):
    """
    Возведение квадратной матрицы A в степень power (целое число ≥ 0).
    Использует алгоритм быстрого возведения в степень.
    """
    if len(A) != len(A[0]):
        raise ValueError("Матрица должна быть квадратной!")
    if power < 0:
        raise ValueError("Степень должна быть неотрицательной!")
    
    n = len(A)
    
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiplication(result, A)
        A = matrix_multiplication(A, A)
        power = power // 2
    
    return result
  
