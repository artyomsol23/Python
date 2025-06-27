def is_latin_square(matrix):
    """
    Проверяет, является ли матрица латинским квадратом.
    
    Латинский квадрат - это квадратная матрица n x n, где каждая строка и каждый столбец
    содержат все числа от 1 до n без повторений.
    
    Аргументы:
    matrix -- двумерный список (квадратная матрица)
    
    Возвращает:
    True, если матрица является латинским квадратом, иначе False
    """
    if not matrix:
        return False
    
    n = len(matrix)
    
    for row in matrix:  # Проверяем, что матрица квадратная
        if len(row) != n:
            return False
    
    for i in range(n):  # Проверяем каждую строку и каждый столбец
        row_elements = set()
        col_elements = set()
        
        for j in range(n):  # Проверяем, что элементы находятся в диапазоне от 1 до n
            if matrix[i][j] < 1 or matrix[i][j] > n:
                return False
            if matrix[j][i] < 1 or matrix[j][i] > n:
                return False
                
            row_elements.add(matrix[i][j])
            col_elements.add(matrix[j][i])
        
        if len(row_elements) != n or len(col_elements) != n:  # Проверяем, что в строке и столбце ровно n уникальных элементов
            return False
    
    return True


# Тесты для функции is_latin_square
def test_is_latin_square():
    assert is_latin_square([[1]]) == True
    assert is_latin_square([[1, 2], [2, 1]]) == True
    assert is_latin_square([[1, 2, 3], [3, 1, 2], [2, 3, 1]]) == True
    assert is_latin_square([[2, 1, 3], [1, 3, 2], [3, 2, 1]]) == True
    assert is_latin_square([]) == False
    assert is_latin_square([[1, 2], [1, 2]]) == False
    assert is_latin_square([[1, 1], [2, 2]]) == False
    assert is_latin_square([[1, 2, 3], [2, 3, 1], [3, 1, 4]]) == False
    assert is_latin_square([[1, 2], [2, 1], [1, 2]]) == False
    assert is_latin_square([[1, 2, 3], [2, 3, 1]]) == False
    
    print("Все тесты пройдены успешно!")

test_is_latin_square()
