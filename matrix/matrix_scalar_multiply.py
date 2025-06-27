def matrix_scalar_multiply(A, c):
    """
    Умножение матрицы A на скаляр c.
    
    Параметры:
    - A (list of lists): Исходная матрица (m × n).
    - c (int/float): Число, на которое умножается матрица.
    
    Возвращает:
    - list of lists: Новая матрица (m × n), где каждый элемент = A[i][j] * c.
    """
    return [[A[i][j] * c for j in range(len(A[0]))] for i in range(len(A))]
  
