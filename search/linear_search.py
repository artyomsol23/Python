def linear_search(arr: list[list[int]], target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1  
