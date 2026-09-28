# AI로 만든 원·사각·삼각 이동 예제
import math
from pico2d import *

def draw(boy, x, y):
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit
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


def polygon(boy, points):
    for start, end in zip(points, points[1:] + points[:1]):
        line(boy, start, end)


def circle(boy):
    for degree in range(0, 361, 5):
        angle = math.radians(degree)
        x = 400 + 200 * math.cos(angle)
        y = 300 + 200 * math.sin(angle)
        draw(boy, x, y)


open_canvas(800, 600)
boy = load_image('character.png')
while True:
    circle(boy)
    polygon(boy, [(50, 50), (50, 550), (750, 550), (750, 50)])
    polygon(boy, [(100, 100), (700, 100), (400, 500)])
close_canvas()
