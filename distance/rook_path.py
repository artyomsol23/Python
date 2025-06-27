def rook_path(start, end):
    x1, y1 = start
    x2, y2 = end
    path = []

    step_x = 1 if x2 > x1 else -1  # Движение по горизонтали
    for x in range(x1, x2, step_x):
        path.append((x + step_x, y1))

    step_y = 1 if y2 > y1 else -1  # Движение по вертикали
    for y in range(y1, y2, step_y):
        path.append((x2, y + step_y))

    return path

start = (0, 0)  # a1
end = (3, 4)    # d5
path = rook_path(start, end)

print("Путь ладьи:", path)  # Вывод: [(1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
