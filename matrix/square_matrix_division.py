def square_matrix_division(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    if len(B) != len(B[0]):
        raise ValueError("Матрица B должна быть квадратной!")
    
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов матрицы A должно равняться числу строк матрицы B!")
    
    B_inv = matrix_inverse(B)
    
    return matrix_multiplication(A, B_inv)
