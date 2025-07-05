def selection_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        min_i = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_idx = j

        arr[i], arr[min_i] = arr[min_i], arr[i]
    
    return arr
