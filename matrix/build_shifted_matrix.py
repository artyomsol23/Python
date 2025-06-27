def build_shifted_matrix(rows, cols, direction="left"):
    """
    Создаёт матрицу размером rows × cols с циклическим сдвигом в каждой строке.
    
    Параметры:
    - rows (int): количество строк в матрице
    - cols (int): количество столбцов в матрице
    - direction (str): направление сдвига ("left" - влево, "right" - вправо)
                      (по умолчанию "left")
    
    Возвращает:
    - list: матрица с циклическим сдвигом в каждой строке
    
    Пример:
    >>> build_shifted_matrix(3, 4)
    [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2]]
    """
    matrix = []
    
    for i in range(rows):
        # Создаём строку с циклическим сдвигом
        if direction == "left":
            # Сдвиг влево: каждый следующий элемент = (текущий индекс + номер строки) % cols + 1
            shifted_row = [(j + i) % cols + 1 for j in range(cols)]
        elif direction == "right":
            # Сдвиг вправо: аналогично, но с обратным направлением
            shifted_row = [(j - i) % cols + 1 for j in range(cols)]
        else:
            raise ValueError("Недопустимое направление сдвига. Используйте 'left' или 'right'")
        
        matrix.append(shifted_row)
    
    return matrix
