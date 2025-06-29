def matrix_multiplication(A: list[list[int]], B: list[list[int]]):
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов A должно равняться числу строк B!")
    
    m, n, k = len(A), len(A[0]), len(B[0])
    
    C = [[0 for _ in range(k)] for _ in range(m)]
    
    for i in range(m):
        for j in range(k):
            for l in range(n):
                C[i][j] += A[i][l] * B[l][j]
    
    return C
