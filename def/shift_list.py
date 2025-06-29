def shift_list(lst: list, k: int, direction="left"):
    if not lst:
        return lst
    
    n = len(lst)
    k %= n  
    
    if direction == "right":  # Направление сдвига — "left" (влево) или "right" (вправо)
        k = -k  
    
    return lst[k:] + lst[:k]
