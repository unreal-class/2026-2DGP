# 실습 과제 진행 - AI 도움을 받아 단계별로 작성
import math
from pico2d import *


def draw(x, y):
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    # 화면 가운데를 중심으로 반지름 200인 원을 한 바퀴 돈다.
    for angle in range(361):
        rad = math.radians(angle)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        draw(x, y)



def move_square():
    draw(50, 550)



def move_triangle():
    draw(100, 100)



open_canvas(800, 600)
boy = load_image('character.png')
while True:
    move_circle()
