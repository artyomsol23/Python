def quick_sort(arr):
    if len(arr) <= 1:  # Если массив содержит 1 элемент или меньше, возвращаем его (база рекурсии)
        return arr
    
    pivot = arr[len(arr) // 2]  # Опорный элемент (можно выбирать по-разному)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы, равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного
    
    return quick_sort(left) + middle + quick_sort(right)  # Рекурсивно сортируем левую и правую части и объединяем результат

# Пример использования
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)
