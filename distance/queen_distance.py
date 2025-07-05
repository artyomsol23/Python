def queen_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    
    if dx == 0 or dy == 0 or dx == dy:
        return max(dx, dy)
    else:
        return 2
