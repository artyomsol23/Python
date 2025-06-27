def transpose_matrix(matrix):
    """
    Транспонирует матрицу (заменяет строки на столбцы).
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    
    return transposed
