def matrix_scalar_multiply_inplace(A, c):
    """Умножение матрицы на скаляр с изменением исходной матрицы."""
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= c
    return A
  
