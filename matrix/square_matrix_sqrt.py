def matrix_sqrt(A: list[list[int]], max_iter=100, tol=1e-6):
    
    if len(A) != len(A[0]):
        raise ValueError("Матрица должна быть квадратной!")

    n = len(A)
    
    X = [[A[i][j] for j in range(n)] for i in range(n)]
    Y = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    
    for _ in range(max_iter):
        inv_Y = matrix_inverse(Y)
        X_new = matrix_scalar_multiply(matrix_addition(X, inv_Y), 0.5)  # X_new = 0.5 * (X + inv_Y)
        
        inv_X = matrix_inverse(X)
        Y_new = matrix_scalar_multiply(matrix_addition(Y, inv_X), 0.5)  # Y_new = 0.5 * (Y + inv_X)
        
        diff = max(abs(X_new[i][j] - X[i][j]) for i in range(n) for j in range(n))
        if diff < tol:
            break
        
        X, Y = X_new, Y_new
    
    return X
