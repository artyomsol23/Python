def matrix_subtraction(A, B):
    """
    Вычитание двух матриц одинакового размера.
    
    Параметры:
        A (list of list): Первая матрица (уменьшаемое).
        B (list of list): Вторая матрица (вычитаемое).
    
    Возвращает:
        list of list: Новая матрица C = A - B.
    
    Исключения:
        ValueError: Если матрицы разного размера.
    """
    # Проверка на одинаковый размер матриц
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Матрицы должны быть одного размера!")
    
    # Получаем количество строк и столбцов
    rows = len(A)
    cols = len(A[0])
    
    # Создаем нулевую матрицу такого же размера
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Поэлементное вычитание
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] - B[i][j]
    
    return C
