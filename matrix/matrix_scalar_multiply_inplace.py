def matrix_scalar_multiply_inplace(A: list[list[int]], c: float) -> float:
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= c
    
    return A
