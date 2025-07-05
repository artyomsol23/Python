def square_matrix_2_or_3_inverse(M: list[list[int]]) -> list[list[int]]:
    n = len(M)
    if n != len(M[0]):
        raise ValueError("Матрица должна быть квадратной!")
    
    if n == 2:
        det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        
        if det == 0:
            raise ValueError("Матрица вырождена (определитель = 0)!")
        
        inv_det = 1.0 / det
        
        return [
            [ M[1][1] * inv_det, -M[0][1] * inv_det],
            [-M[1][0] * inv_det,  M[0][0] * inv_det]
        ]
        
    elif n == 3:
        raise NotImplementedError("Обратная матрица 3×3 здесь не реализована.")
        
    else:
        raise ValueError("Функция поддерживает только матрицы 2×2 и 3×3.")
