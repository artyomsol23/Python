def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивная реализация бинарного поиска в отсортированном массиве.
    
    Параметры:
        arr (list): Отсортированный массив, в котором выполняется поиск.
        target: Искомый элемент.
        left (int): Левая граница диапазона поиска (индекс).
        right (int): Правая граница диапазона поиска (индекс).
        
    Возвращает:
        int: Индекс искомого элемента, если найден, иначе -1.
    """
    
    # Базовый случай: элемент не найден
    if left > right:
        return -1
    
    # Находим середину текущего диапазона
    mid = (left + right) // 2
    
    # Если элемент в середине - искомый, возвращаем его индекс
    if arr[mid] == target:
        return mid
    # Если искомый элемент больше элемента в середине, ищем в правой половине
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    # Иначе ищем в левой половине
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
