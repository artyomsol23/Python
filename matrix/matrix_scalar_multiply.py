def matrix_scalar_multiply(A: list[list[int]], c: float) -> float:
    result = [[0.0 for _ in range(len(A[0]))] for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] * c
    
    return result
