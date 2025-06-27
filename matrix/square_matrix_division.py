def square_matrix_division(A, B):
    """
    Деление матриц A на B (A × обратная(B)).
    Возвращает матрицу C = A × B^(-1).
    """
    if len(B) != len(B[0]):
        raise ValueError("Матрица B должна быть квадратной!")
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов A должно равняться числу строк B!")
    
    B_inv = matrix_inverse(B)
    return matrix_multiplication(A, B_inv)
