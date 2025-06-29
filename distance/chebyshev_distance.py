def chebyshev_distance(a: tuple[float, float], b: tuple[float, float]):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    
    return max(dx, dy)
