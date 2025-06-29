def rook_path(start: tuple[int, int], end: tuple[int, int]):
    x1, y1 = start
    x2, y2 = end
    path = []

    step_x = 1 if x2 > x1 else -1
    for x in range(x1, x2, step_x):
        path.append((x + step_x, y1))

    step_y = 1 if y2 > y1 else -1
    for y in range(y1, y2, step_y):
        path.append((x2, y + step_y))

    return path
