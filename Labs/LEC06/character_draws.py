from os.path import abspath, dirname, join
import math
from pico2d import *

open_canvas(800, 600)
#어떤 이유에서인지 character.png파일이 제대로 불러와지지 않아 해당 부분은 ai를 통해 수정하였습니다.
image_path = join(dirname(abspath(__file__)), 'character.png')
boy = load_image(image_path)

def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

degree = 0
theta = math.radians(degree)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)

def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, 550)


def move_right():
    for y in range(550, 49, -5):
        draw_boy(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        draw_boy(x, 50)


def move_left():
    for y in range(50, 551, 5):
        draw_boy(50, y)


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_triangle():
    for i in range(101):
        t = i / 100
        x = 400 + (750 - 400) * t
        y = 550 + (50 - 550) * t
        draw_boy(x, y)

    for i in range(101):
        t = i / 100
        x = 750 + (50 - 750) * t
        y = 50
        draw_boy(x, y)

    for i in range(101):
        t = i / 100
        x = 50 + (400 - 50) * t
        y = 50 + (550 - 50) * t
        draw_boy(x, y)

while True:
    move_circle()
    move_rectangle()
    move_triangle()
