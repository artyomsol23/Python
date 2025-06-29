def transpose_matrix(matrix: list[list[int]]):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0  # Проверяем случай пустой матрицы

    for i in range(cols):
        for j in range(rows):
            transposed = matrix[j][i]
    
    return transposed
