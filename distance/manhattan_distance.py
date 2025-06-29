def manhattan_distance(a: tuple[int, int], b: tuple[int, int]):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    
    return dx + dy
