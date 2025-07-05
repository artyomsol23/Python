def square_matrix_power(A: list[list[int]], power: int) -> int:
    if len(A) != len(A[0]):
        raise ValueError("Матрица должна быть квадратной!")
    
    if power < 0:
        raise ValueError("Степень должна быть неотрицательной!")
    
    result = [[0] * len(A) for _ in range(len(A))]

    for i in range(len(A)):
        result[i][i] = 1
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_multiplication(result, A)
        A = matrix_multiplication(A, A)
        power = power // 2
    
    return result
