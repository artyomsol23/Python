def euclidean_distance_sq(a: tuple[float, float], b: tuple[float, float]) -> float:
    dx_sq = (a[0] - b[0]) ** 2    
    dy_sq = (a[1] - b[1]) ** 2
    
    return dx_sq + dy_sq
