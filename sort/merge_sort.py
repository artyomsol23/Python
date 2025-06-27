def merge_sort(arr):
    """
    Сортировка слиянием (Merge Sort)
    
    Параметры:
        arr (list): Неотсортированный массив
    
    Возвращает:
        list: Отсортированный массив
    """
    
    # Базовый случай: если массив пуст или состоит из одного элемента, возвращаем его
    if len(arr) <= 1:
        return arr
    
    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Объединяем отсортированные половины
    return merge(left_half, right_half)

def merge(left, right):
    """
    Функция слияния двух отсортированных массивов
    
    Параметры:
        left (list): Левый отсортированный массив
        right (list): Правый отсортированный массив
    
    Возвращает:
        list: Объединенный отсортированный массив
    """
    
    result = []
    left_idx, right_idx = 0, 0  # Индексы для перебора элементов
    
    # Сливаем элементы, пока не достигнем конца одного из массивов
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Добавляем оставшиеся элементы из левого массива (если они есть)
    result.extend(left[left_idx:])
    
    # Добавляем оставшиеся элементы из правого массива (если они есть)
    result.extend(right[right_idx:])
    
    return result  # Возвращаем отсортированный массив
