# 실습 과제 진행 - AI 도움을 받아 단계별로 작성
import math
from pico2d import *

def draw_circle():
    for degree in range(0, 360, 5):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)

def move_top():
    print('top')
    for y in range(50, 551, 10):
        draw_character(50, y)
    

def draw_character(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.05)

def move_right():
    print('right')
    for x in range(50, 751, 10):
           draw_character(x, 550)

def move_bottom():
    print('bottom')
    for y in range(550, 49, -10):
        draw_character(750, y)

def move_left():
    print('left')
    for x in range(750, 49, -10):
        draw_character(x, 50)


def draw_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def triangle_bottom():
    for x in range(100, 701, 10):
        draw_character(x, 100)


def triangle_up():
    for step in range(51):
        x = 700 - 300 * step / 50
        y = 100 + 400 * step / 50
        draw_character(x, y)


def triangle_down():
    for step in range(51):
        x = 400 - 300 * step / 50
        y = 500 - 400 * step / 50
        draw_character(x, y)


def draw_triangle():
    triangle_bottom()
    triangle_up()
    triangle_down()

open_canvas(800, 600)
boy = load_image('character.png')
while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
