def loss(x: float, y: float, w: list) -> float:
    return (a(x, w) - y) ** 2 

def calculate_mse(coord_x: list, coord_y: list, w: list) -> float:
    total_loss = 0.0
    
    for i in range(len(coord_x)):
        total_loss += loss(coord_x[i], coord_y[i], w)
    
    return total_loss / len(coord_x)  # mean squared error

Q = calculate_mse(coord_x, coord_y, w)
