def is_symmetric_main(matrix):
    """Проверяет, является ли матрица симметричной относительно главной диагонали."""
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    if rows != cols:  # Проверка, что матрица квадратная
        return False
    
    for i in range(rows):
        for j in range(i + 1, cols):  # Проверяем только элементы выше диагонали
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Пример использования
matrix_symmetric_main = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6],
]

matrix_non_symmetric_main = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(is_symmetric(matrix_symmetric_main))  # True
print(is_symmetric(matrix_non_symmetric_main))  # False
