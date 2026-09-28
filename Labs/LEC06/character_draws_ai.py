from pico2d import *
import math

open_canvas(800, 600)

boy = load_image('character.png')


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)

        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_boy(x, y)


def move_rectangle():
    # 위쪽: 왼쪽 -> 오른쪽
    for x in range(50, 751, 5):
        draw_boy(x, 550)

    # 오른쪽: 위쪽 -> 아래쪽
    for y in range(550, 49, -5):
        draw_boy(750, y)

    # 아래쪽: 오른쪽 -> 왼쪽
    for x in range(750, 49, -5):
        draw_boy(x, 50)

    # 왼쪽: 아래쪽 -> 위쪽
    for y in range(50, 551, 5):
        draw_boy(50, y)


def move_line(x1, y1, x2, y2):
    steps = 100

    for i in range(steps + 1):
        t = i / steps

        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        draw_boy(x, y)


def move_triangle():
    # 위 꼭짓점 -> 오른쪽 아래
    move_line(400, 550, 750, 50)

    # 오른쪽 아래 -> 왼쪽 아래
    move_line(750, 50, 50, 50)

    # 왼쪽 아래 -> 위 꼭짓점
    move_line(50, 50, 400, 550)


while True:
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()