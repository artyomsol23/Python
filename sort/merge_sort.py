def merge_sort(arr):
    if len(arr) <= 1:  # Проверяем, не является ли массив пустым или состоящим из одного элемента
        return arr
    
    mid = len(arr) // 2  # Разделяем массив на две половины
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)  # Рекурсивно сортируем каждую половину
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)  # Объединяем отсортированные половины

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left) and right_idx < len(right):  # Сливаем элементы, пока не достигнем конца одного из массивов
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Добавляем оставшиеся элементы (если они есть)
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result

# Пример использования
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Исходный массив:", arr)
    sorted_arr = merge_sort(arr)
    print("Отсортированный массив:", sorted_arr)
