def bubble_sort(arr: list):
    n = len(arr)
    
    for i in range(n):
        flag = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
                
        if not flag:
            break
            
    return arr
