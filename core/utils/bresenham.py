from core.models.point import Point


def bresenham(source_point, destination_point):
    x0, y0 = source_point.x, source_point.y
    x1, y1 = destination_point.x, destination_point.y
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)
    line = []
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    dif = dx - dy
    while True:
        line.append(Point(x0, y0))
        if x0 == x1 and y0 == y1:
            return line
        dif2 = 2 * dif
        if dif2 > -dy:
            dif = dif - dy
            x0 = x0 + sx
        if dif2 < dx:
            dif = dif + dx
            y0 = y0 + sy
