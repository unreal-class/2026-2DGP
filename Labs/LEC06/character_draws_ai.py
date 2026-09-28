# AI로 만든 원·사각·삼각 이동 예제
import math
from pico2d import *

FPS = 60
SPEED = 400  # 초당 이동할 거리

def draw(boy, x, y):
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(1 / FPS)


def line(start, end):
    if start == end:
        return [start]
    x1, y1 = start
    x2, y2 = end
    gap = SPEED / FPS
    count = max(1, math.ceil(math.hypot(x2 - x1, y2 - y1) / gap))
    points = []
    for n in range(count + 1):
        x = x1 + (x2 - x1) * n / count
        y = y1 + (y2 - y1) * n / count
        points.append((x, y))
    return points


def polygon(points):
    path = []
    for start, end in zip(points, points[1:] + points[:1]):
        path.extend(line(start, end)[:-1])
    path.append(points[0])
    return path


def circle():
    count = math.ceil(2 * math.pi * 200 / (SPEED / FPS))
    points = []
    for n in range(count + 1):
        angle = 2 * math.pi * n / count
        x = 400 + 200 * math.cos(angle)
        y = 300 + 200 * math.sin(angle)
        points.append((x, y))
    return points


open_canvas(800, 600)
boy = load_image('character.png')
square = [(50, 50), (50, 550), (750, 550), (750, 50)]
triangle = [(100, 100), (700, 100), (400, 500)]
while True:
    paths = (circle(), polygon(square), polygon(triangle))
    for points in paths:
        for x, y in points:
            draw(boy, x, y)
close_canvas()
