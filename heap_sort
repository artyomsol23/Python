def heapify(arr, n, i):
    """
    Функция для преобразования поддерева в двоичную кучу
    :param arr: массив
    :param n: размер кучи
    :param i: корневой индекс поддерева
    """
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый дочерний элемент
    right = 2 * i + 2  # Правый дочерний элемент

    if left < n and arr[left] > arr[largest]:  # Если левый дочерний элемент больше корня
        largest = left

    if right < n and arr[right] > arr[largest]:  # Если правый дочерний элемент больше, чем самый большой элемент на данный момент
        largest = right

    if largest != i:  # Если самый большой элемент не корень
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        heapify(arr, n, largest)  # Рекурсивно преобразуем затронутое поддерево

def heap_sort(arr):
    """
    Основная функция для сортировки массива заданного размера
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):  # Построение max-heap
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):  # Один за другим извлекаем элементы из кучи
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами
        heapify(arr, i, 0)  # Вызываем heapify на уменьшенной куче

# Пример использования
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Исходный массив:")
    print(arr)
    
    heap_sort(arr)
    print("Отсортированный массив:")
    print(arr)
