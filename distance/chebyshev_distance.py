def chebyshev_distance(a: tuple[float, float], b: tuple[float, float]):
    dx = abs(a[0] - b[0])  # Разность по оси X
    dy = abs(a[1] - b[1])  # Разность по оси Y
    
    return max(dx, dy)
