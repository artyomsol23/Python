def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left: list, right: list) -> list:
    result = []
    left_i, right_i = 0, 0
    
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    
    return result
