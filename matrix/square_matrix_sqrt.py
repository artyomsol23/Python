def matrix_sqrt(A, max_iter=100, tol=1e-6):
    """
    Вычисление квадратного корня матрицы методом Ньютона-Шульца.
    Поддерживает только квадратные матрицы небольшого размера (2×2 или 3×3).
    """
    n = len(A)
    if n != len(A[0]):
        raise ValueError("Матрица должна быть квадратной!")
    
    X = [[A[i][j] for j in range(n)] for i in range(n)]  # Инициализация: X = A, Y = I (единичная матрица)
    Y = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    for _ in range(max_iter):
        inv_Y = matrix_inverse(Y)
        X_new = matrix_scalar_multiply(matrix_addition(X, inv_Y), 0.5)  # X_new = 0.5 * (X + inverse(Y))
        
        inv_X = matrix_inverse(X)
        Y_new = matrix_scalar_multiply(matrix_addition(Y, inv_X), 0.5)  # Y_new = 0.5 * (Y + inverse(X))
        
        diff = max(abs(X_new[i][j] - X[i][j]) for i in range(n) for j in range(n))  # Проверка на сходимость (по норме разности)
        if diff < tol:
            break
        
        X, Y = X_new, Y_new
    
    return X
