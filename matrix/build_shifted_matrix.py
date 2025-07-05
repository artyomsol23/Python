def build_shifted_matrix(rows: int, cols: int, direction: str = "left") -> list[list[int]]:
    matrix = []
    
    for i in range(rows):
        if direction == "left":
            shifted_row = [(j + i) % cols + 1 for j in range(cols)]
        elif direction == "right":
            shifted_row = [(j - i) % cols + 1 for j in range(cols)]
        else:
            raise ValueError("Недопустимое направление сдвига. Используйте 'left' или 'right'")
        
        matrix.append(shifted_row)
    
    return matrix
