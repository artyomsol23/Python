def euclidean_distance(a: tuple[float, float], b: tuple[float, float]):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    
    distance = (dx ** 2 + dy ** 2) ** 0.5
    
    return distance
