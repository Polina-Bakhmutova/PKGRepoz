import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.collections import LineCollection

def draw_line(ax, x1, y1, x2, y2, color='blue'):
    line = [(x1, y1), (x2, y2)]
    ax.add_collection(LineCollection([line], colors=color))
    ax.plot([x1, x2], [y1, y2], 'o', color=color)

def draw_rectangle(ax, xmin, ymin, xmax, ymax):
    rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor='red', facecolor='none')
    ax.add_patch(rect)

def clip_line(ax, x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    x1, y1, x2, y2 = clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, 'x')
    x1, y1, x2, y2 = clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, 'y')
    draw_line(ax, x1, y1, x2, y2, color='green')

def clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax, coordinate):
    dx, dy = x2 - x1, y2 - y1

    m = dy / dx if dx != 0 else float('inf')

    def intersect(x, y):
        if x1 <= x <= x2 and ymin <= y <= ymax:
            return True, (x, y)
        elif xmin <= x <= xmax and y1 <= y <= y2:
            return True, (x, y)
        return False, (0, 0)

    if coordinate == 'x':
        if x1 < xmin and x2 < xmin:
            return 0, 0, 0, 0
        elif x1 > xmax and x2 > xmax:
            return 0, 0, 0, 0
        elif x1 < xmin and xmin <= x2 <= xmax:
            intersects, p = intersect(xmin, y1 + (xmin - x1) * m)
            if intersects:
                x1, y1 = p
        elif x2 < xmin and xmin <= x1 <= xmax:
            intersects, p = intersect(xmin, y2 + (xmin - x2) * m)
            if intersects:
                x2, y2 = p
        elif x1 > xmax and xmin <= x2 <= xmax:
            intersects, p = intersect(xmax, y1 + (xmax - x1) * m)
            if intersects:
                x1, y1 = p
        elif x2 > xmax and xmin <= x1 <= xmax:
            intersects, p = intersect(xmax, y2 + (xmax - x2) * m)
            if intersects:
                x2, y2 = p
    elif coordinate == 'y':
        if y1 < ymin and y2 < ymin:
            return 0, 0, 0, 0
        elif y1 > ymax and y2 > ymax:
            return 0, 0, 0, 0
        elif y1 < ymin and ymin <= y2 <= ymax:
            intersects, p = intersect(x1 + (ymin - y1) / m, ymin)
            if intersects:
                x1, y1 = p
        elif y2 < ymin and ymin <= y1 <= ymax:
            intersects, p = intersect(x2 + (ymin - y2) / m, ymin)
            if intersects:
                x2, y2 = p
        elif y1 > ymax and ymin <= y2 <= ymax:
            intersects, p = intersect(x1 + (ymax - y1) / m, ymax)
            if intersects:
                x1, y1 = p
        elif y2 > ymax and ymin <= y1 <= ymax:
            intersects, p = intersect(x2 + (ymax - y2) / m, ymax)
            if intersects:
                x2, y2 = p

    return x1, y1, x2, y2

def main():
    fig, ax = plt.subplots()

    # Исходные данные
    lines = [(50, 30, 150, 130), (120, 100, 200, 20), (10, 80, 120, 80)]
    xmin, ymin, xmax, ymax = 70, 50, 170, 120

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    draw_rectangle(ax, xmin, ymin, xmax, ymax)

    for line in lines:
        draw_line(ax, *line, color='blue')

    for line in lines:
        clip_line(ax, *line, xmin, ymin, xmax, ymax)

    plt.show()

if __name__ == "__main__":
    main()
