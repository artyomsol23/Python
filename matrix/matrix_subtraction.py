def matrix_subtraction(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Матрицы должны быть одного размера!")
    
    rows, cols = len(A), len(A[0])
    
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] - B[i][j]
    
    return C
