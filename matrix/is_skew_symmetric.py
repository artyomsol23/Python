def is_skew_symmetric(matrix: list[list[int]]) -> bool:
    n = len(matrix)
    
    for row in matrix:
        if len(row) != n:
            return False
    
    for i in range(n):
        for j in range(n - i):
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return False
    
    return True
