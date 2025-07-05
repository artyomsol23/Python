def king_moves(start: tuple[int, int], end:tuple[int, int]) -> int:
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    return max(dx, dy)
    
