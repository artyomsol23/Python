def binary_search_recursive(arr, target, left, right):
    """
    Рекурсивная реализация бинарного поиска в отсортированном по возрастанию массиве.
    
    Параметры:
        arr (list): Отсортированный по возрастанию массив, в котором выполняется поиск.
        target: Искомый элемент (должен быть сравним с элементами массива).
        left (int): Левая граница диапазона поиска (индекс).
        right (int): Правая граница диапазона поиска (индекс).
        
    Возвращает:
        int: Индекс искомого элемента, если найден, иначе -1.
        
    Примеры:
        >>> binary_search_recursive([1, 2, 3, 4], 3, 0, 3)
        2
        >>> binary_search_recursive([1, 2, 3, 4], 5, 0, 3)
        -1
    """
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
