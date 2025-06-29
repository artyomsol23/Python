def matrix_scalar_multiply(A: list[list[int]], c: float):
    return [[A[i][j] * c for j in range(len(A[0]))] for i in range(len(A))]
