def quicksort_inplace(arr, low=0, high=None):
    """
    Быстрая сортировка (quicksort) на месте (in-place) для массива arr.
    
    Параметры:
        arr (list): Сортируемый массив.
        low (int): Начальный индекс для сортировки (по умолчанию 0).
        high (int): Конечный индекс для сортировки (по умолчанию len(arr) - 1).
    """
    if high is None:
        high = len(arr) - 1
    
    # Рекурсивно сортируем элементы до и после разбиения
    if low < high:
        # Индекс разбиения, arr[partition_index] теперь на правильном месте
        partition_index = partition(arr, low, high)  
        
        # Сортируем левую часть от опорного элемента
        quicksort_inplace(arr, low, partition_index - 1)
        # Сортируем правую часть от опорного элемента
        quicksort_inplace(arr, partition_index + 1, high)


def partition(arr, low, high):
    """
    Вспомогательная функция для разбиения массива относительно опорного элемента.
    
    Параметры:
        arr (list): Массив для разбиения.
        low (int): Начальный индекс диапазона.
        high (int): Конечный индекс диапазона.
        
    Возвращает:
        int: Индекс опорного элемента после разбиения.
    """
    # Выбираем последний элемент как опорный (pivot)
    pivot = arr[high]  
    
    # Индекс меньшего элемента, указывает на правильную позицию pivot
    i = low - 1  
    
    # Проходим по всем элементам в диапазоне [low, high-1]
    for j in range(low, high):
        # Если текущий элемент меньше или равен pivot
        if arr[j] <= pivot:
            i += 1
            # Меняем местами элементы arr[i] и arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Помещаем pivot на правильную позицию (между меньшими и большими элементами)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Возвращаем индекс опорного элемента
    return i + 1
