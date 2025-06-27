def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed
  
