import pygame
import sys
import math

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Растровые алгоритмы")

# Параметры для отрисовки линии пошаговым алгоритмом
line_step_start = (50, 50)
line_step_end = (300, 150)

# Параметры для отрисовки линии алгоритмом ЦДА
line_dda_start = (50, 200)
line_dda_end = (100, 100)

# Параметры для отрисовки линии алгоритмом Брезенхема
line_bresenham_start = (50, 400)
line_bresenham_end = (300, 500)

# Параметры для отрисовки окружности алгоритмом Брезенхема
circle_bresenham_center = (600, 300)
circle_bresenham_radius = 50

# Параметры для отрисовки окружности алгоритмом Кастла-Питвея
circle_castle_pitway_center = (600, 100)
circle_castle_pitway_radius = 50


def draw_line_step(start, end):
    x, y = start
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    for _ in range(steps):
        pygame.draw.circle(screen, white, (round(x), round(y)), 1)
        x += x_increment
        y += y_increment


def draw_line_dda(start, end):
    x, y = start
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    for _ in range(steps):
        pygame.draw.circle(screen, white, (round(x), round(y)), 1)
        x += x_increment
        y += y_increment


def draw_line_bresenham(start, end):
    x, y = start
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    steps = max(abs(dx), abs(dy))
    x_increment = dx / steps
    y_increment = dy / steps

    x_rounded, y_rounded = round(x), round(y)

    for _ in range(steps):
        pygame.draw.circle(screen, white, (x_rounded, y_rounded), 1)
        x += x_increment
        y += y_increment
        x_rounded, y_rounded = round(x), round(y)


def draw_circle_bresenham(center, radius):
    x, y = center
    p = 3 - 2 * radius

    points = set()

    def draw_symmetric_points(cx, cy, x, y):
        pygame.draw.circle(screen, white, (cx + x, cy + y), 1)
        pygame.draw.circle(screen, white, (cx - x, cy + y), 1)
        pygame.draw.circle(screen, white, (cx + x, cy - y), 1)
        pygame.draw.circle(screen, white, (cx - x, cy - y), 1)
        pygame.draw.circle(screen, white, (cx + y, cy + x), 1)
        pygame.draw.circle(screen, white, (cx - y, cy + x), 1)
        pygame.draw.circle(screen, white, (cx + y, cy - x), 1)
        pygame.draw.circle(screen, white, (cx - y, cy - x), 1)

    x = 0
    y = radius
    draw_symmetric_points(center[0], center[1], x, y)

    while x <= y:
        x += 1
        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6
        draw_symmetric_points(center[0], center[1], x, y)


def draw_circle_castle_pitway(center, radius):
    x, y = center
    p = 1 - radius
    x, y = 0, radius

    def draw_symmetric_points(cx, cy, x, y):
        pygame.draw.circle(screen, white, (cx + x, cy - y), 1)
        pygame.draw.circle(screen, white, (cx - x, cy - y), 1)
        pygame.draw.circle(screen, white, (cx + x, cy + y), 1)
        pygame.draw.circle(screen, white, (cx - x, cy + y), 1)

    draw_symmetric_points(center[0], center[1], x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        draw_symmetric_points(center[0], center[1], x, y)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Очищаем экран
        screen.fill(black)

        # Рисуем линии и окружности различными алгоритмами
        draw_line_step(line_step_start, line_step_end)
        draw_line_dda(line_dda_start, line_dda_end)
        draw_line_bresenham(line_bresenham_start, line_bresenham_end)
        draw_circle_bresenham(circle_bresenham_center, circle_bresenham_radius)
        draw_circle_castle_pitway(circle_castle_pitway_center, circle_castle_pitway_radius)

        # Обновляем экран
        pygame.display.flip()


if __name__ == "__main__":
    main()
#отрезок право вниз