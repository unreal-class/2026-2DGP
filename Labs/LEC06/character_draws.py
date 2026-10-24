from pico2d import *
import math

# 캔버스 변수
canvas_x = 800
canvas_y = 600
# 딜레이 변수
idx = 0.05

# 사각형 위치 변수
rec_move_t1 = [400, 750]
rec_move_t2 = [50, 400]
rec_move_r = [550, 50]
rec_move_b = [750, 50]
rec_move_l = [50, 550]

# 삼각형 위치 변수
tri_point1 = [400, 550]
tri_point2 = [750, 50]
tri_point3 = [50, 50]
# 삼각형 각도
steps = 120

# 캔버스 생성
open_canvas(canvas_x, canvas_y)


# 이미지 로드
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(idx)

def move_circle():
    for degree in range(90, 90 + 360, 20):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_character(x, y)
    pass

def move_top1():
    print(f"top")
    for x in range(rec_move_t1[0], rec_move_t1[1], 20):
        draw_character(x, 550)
    pass

def move_top2():
    print(f"top")
    for x in range(rec_move_t2[0], rec_move_t2[1], 20):
        draw_character(x, 550)
    pass

def move_right():
    print(f"right")
    for y in range(rec_move_r[0], rec_move_r[1], -20):
        draw_character(750, y)
    pass

def move_bottom():
    print(f"bottom")
    for x in range(rec_move_b[0], rec_move_b[1], -20):
        draw_character(x, 50)
    pass

def move_left():
    print(f"left")
    for y in range(rec_move_l[0], rec_move_l[1], 20):
        draw_character(50, y)
    pass

def move_rectangle():
    move_top1()
    move_right()
    move_bottom()
    move_left()
    move_top2()
    pass

def move_between(start_x, start_y, end_x, end_y):
    for step in range(steps + 1):
        t = step / steps
        x = start_x + (end_x - start_x) * t
        y = start_y + (end_y - start_y) * t
        draw_character(x, y)

def move_triangle():
    move_between(tri_point1[0], tri_point1[1], tri_point2[0], tri_point2[1])
    move_between(tri_point2[0], tri_point2[1], tri_point3[0], tri_point3[1])
    move_between(tri_point3[0], tri_point3[1], tri_point1[0], tri_point1[1])
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    print(f"cycling")
    pass

close_canvas()