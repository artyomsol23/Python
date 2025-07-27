def loss(x: float, y: float, w: list) -> float:
    return (a(x, w) - y) ** 2 

def calculate_mse(coord_x: list, coord_y: list, w: list) -> float:
    total_loss = 0.0
    sz = len(coord_x)
    
    for i in range(sz):
        total_loss += loss(coord_x[i], coord_y[i], w)
    
    return total_loss / sz  # mean squared error

Q = calculate_mse(coord_x, coord_y, w)
