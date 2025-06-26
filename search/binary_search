def binary_search(arr, target):
    """
    Бинарный поиск элемента target в отсортированном массиве arr.
    Возвращает индекс элемента, если он найден, или -1, если не найден.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Находим середину текущего диапазона
        
        if arr[mid] == target:
            return mid  # Элемент найден
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине
    
    return -1  # Элемент не найден


# Пример использования
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Элемент {target_value} найден по индексу {result}.")
else:
    print(f"Элемент {target_value} не найден в массиве.")
