def is_skew_symmetric(matrix):
    """Проверяет, является ли матрица симметричной относительно побочной диагонали."""
    n = len(matrix)
    
    # Проверка на квадратность
    for row in matrix:
        if len(row) != n:
            return False
    
    # Проверка элементов
    for i in range(n):
        for j in range(n - i):  # Проверяем только элементы "до" побочной диагонали
            if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
                return False
    return True

# Пример использования
matrix_skew_symmetric = [
    [3, 2, 1],
    [4, 5, 2],
    [7, 4, 3],
]

matrix_non_skew_symmetric = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(is_skew_symmetric(matrix_skew_symmetric))      # True
print(is_skew_symmetric(matrix_non_skew_symmetric))  # False
