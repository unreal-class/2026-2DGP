# 실습 과제 진행 - AI 도움을 받아 단계별로 작성
from pico2d import *


def draw(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    draw(600, 300)



def move_square():
    draw(50, 550)



def move_triangle():
    draw(100, 100)



open_canvas(800, 600)
boy = load_image('character.png')
move_circle()
move_square()
move_triangle()
delay(1)
close_canvas()
