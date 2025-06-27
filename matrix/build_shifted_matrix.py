def build_shifted_matrix(rows, cols, direction="left"):
    """
    Создаёт матрицу rows × cols с циклическим сдвигом в каждой строке.
    """
    matrix = []
    for i in range(rows):
        shifted_row = [(j + i) % cols + 1 for j in range(cols)]
        matrix.append(shifted_row)
    return matrix
    
