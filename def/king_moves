def king_moves(start, end):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy)  # Расстояние Чебышёва

# Пример:
start = (0, 0)  # a1
end = (7, 7)    # h8
print(f"Минимальное число ходов короля: {king_moves(start, end)}")  # 7
