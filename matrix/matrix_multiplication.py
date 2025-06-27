def matrix_multiplication(A, B):
    """
    Умножение матриц A (m × n) на B (n × k).
    Возвращает матрицу C (m × k) = A × B.
    """
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов A должно равняться числу строк B!")
    
    m = len(A)
    n = len(A[0])
    k = len(B[0])
    
    C = [[0 for _ in range(k)] for _ in range(m)]
    
    for i in range(m):
        for j in range(k):
            for l in range(n):
                C[i][j] += A[i][l] * B[l][j]
    
    return C
  
