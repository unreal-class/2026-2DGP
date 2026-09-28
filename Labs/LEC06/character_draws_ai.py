# AI로 만든 원·사각·삼각 이동 예제
import math
from pico2d import *

def draw(boy, x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.02)


def line(boy, start, end):
    if start == end:
        draw(boy, *start)
        return
    x1, y1 = start
    x2, y2 = end
    count = max(1, math.ceil(math.hypot(x2 - x1, y2 - y1) / 10))
    for n in range(count + 1):
        x = x1 + (x2 - x1) * n / count
        y = y1 + (y2 - y1) * n / count
        draw(boy, x, y)


open_canvas(800, 600)
boy = load_image('character.png')
line(boy, (50, 50), (50, 550))
close_canvas()
