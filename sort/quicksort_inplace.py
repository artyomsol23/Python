def quicksort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:  # Рекурсивно сортируем элементы до и после разбиения
        partition_index = partition(arr, low, high)  # partition_index - индекс разбиения, arr[partition_index] теперь на правильном месте
        quicksort_inplace(arr, low, partition_index - 1)
        quicksort_inplace(arr, partition_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Выбираем последний элемент как опорный
    i = low - 1  # Индекс меньшего элемента
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
