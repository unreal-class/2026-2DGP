# Drill 08: AI를 이용한 애니메이션 뷰어
import json
from pico2d import *

WIDTH, HEIGHT = 800, 600
SCALE = 1

def draw_frame(sheet, frame):
    box = frame['frame']
    w, h = box['w'], box['h']
    x, y = WIDTH / 2, HEIGHT / 2
    clear_canvas()
    # JSON은 위에서부터, pico2d는 아래에서부터 y 좌표를 센다.
    sheet.clip_draw(box['x'], sheet.h - box['y'] - h, w, h,
                    x, y, w * SCALE, h * SCALE)
    update_canvas()


open_canvas(WIDTH, HEIGHT)
sheet = load_image('viewer_knight.png')
with open('viewer_knight.json', encoding='utf-8') as file:
    data = json.load(file)
all_frames = data['textures'][0]['frames']
draw_frame(sheet, all_frames[0])
delay(0.2)
close_canvas()
