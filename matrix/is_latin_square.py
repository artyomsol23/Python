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
    # Проверка на пустую матрицу
    if not matrix:
        return False
    
    n = len(matrix)
    
    # Проверка, что матрица квадратная (все строки имеют длину n)
    for row in matrix:
        if len(row) != n:
            return False
    
    # Проверка каждой строки и каждого столбца
    for i in range(n):
        row_elements = set()  # Множество для элементов строки
        col_elements = set()  # Множество для элементов столбца
        
        for j in range(n):
            # Проверка, что элемент строки находится в диапазоне [1, n]
            if matrix[i][j] < 1 or matrix[i][j] > n:
                return False
            # Проверка, что элемент столбца находится в диапазоне [1, n]
            if matrix[j][i] < 1 or matrix[j][i] > n:
                return False
            
            # Добавляем элементы в множества
            row_elements.add(matrix[i][j])
            col_elements.add(matrix[j][i])
        
        # Проверка, что в строке и столбце ровно n уникальных элементов
        if len(row_elements) != n or len(col_elements) != n:
            return False
    
    # Если все проверки пройдены, возвращаем True
    return True
