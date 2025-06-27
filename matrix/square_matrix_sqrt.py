def matrix_sqrt(A, max_iter=100, tol=1e-6):
    """
    Вычисление квадратного корня матрицы методом Ньютона-Шульца.
    
    Параметры:
    ----------
    A : list of list of float
        Входная квадратная матрица (2×2 или 3×3).
    max_iter : int, optional
        Максимальное количество итераций (по умолчанию 100).
    tol : float, optional
        Допустимая погрешность для проверки сходимости (по умолчанию 1e-6).
    
    Возвращает:
    -----------
    list of list of float
        Матрица, являющаяся квадратным корнем из A.
    
    Исключения:
    -----------
    ValueError
        Если входная матрица не квадратная.
    """
    
    # Проверка, что матрица квадратная
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Матрица должна быть квадратной!")
    
    # Инициализация:
    # X = A (начальное приближение)
    # Y = I (единичная матрица)
    X = [[A[i][j] for j in range(n)] for i in range(n)]
    Y = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    # Итерационный процесс Ньютона-Шульца
    for _ in range(max_iter):
        # Вычисление новых приближений X и Y
        inv_Y = matrix_inverse(Y)
        X_new = matrix_scalar_multiply(matrix_addition(X, inv_Y), 0.5)  # X_new = 0.5 * (X + inv_Y)
        
        inv_X = matrix_inverse(X)
        Y_new = matrix_scalar_multiply(matrix_addition(Y, inv_X), 0.5)  # Y_new = 0.5 * (Y + inv_X)
        
        # Проверка сходимости: максимальное изменение в матрице X
        diff = max(abs(X_new[i][j] - X[i][j]) for i in range(n) for j in range(n))
        if diff < tol:
            break
        
        # Обновление значений для следующей итерации
        X, Y = X_new, Y_new
    
    return X
