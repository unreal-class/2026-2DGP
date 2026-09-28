# AI로 만든 원·사각·삼각 이동 예제
from pico2d import *

def draw(boy, x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.02)


open_canvas(800, 600)
boy = load_image('character.png')
draw(boy, 400, 300)
delay(0.1)
close_canvas()
