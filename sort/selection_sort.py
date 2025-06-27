def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Находим минимальный элемент в оставшейся части
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Меняем найденный минимальный элемент с первым неотсортированным
    
    return arr

# Пример использования
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Отсортированный массив:", sorted_array)
