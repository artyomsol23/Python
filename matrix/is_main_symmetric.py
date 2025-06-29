def is_main_symmetric(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if rows != cols:
        return False
    
    for i in range(rows):
        for j in range(i + 1, cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
