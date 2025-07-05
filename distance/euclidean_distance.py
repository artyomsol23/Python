def euclidean_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    
    return (dx ** 2 + dy ** 2) ** 0.5
