def is_latin_square(matrix: list[list[int]]) -> bool:
    if not matrix:
        return False
    
    n = len(matrix)
    
    for row in matrix:
        if len(row) != n:
            return False
    
    for i in range(n):
        row_elements, col_elements = set(), set()
        for j in range(n):
            if matrix[i][j] < 1 or matrix[i][j] > n:
                return False
            if matrix[j][i] < 1 or matrix[j][i] > n:
                return False
            
            row_elements.add(matrix[i][j])
            col_elements.add(matrix[j][i])
        
        if len(row_elements) != n or len(col_elements) != n:
            return False
    
    return True
