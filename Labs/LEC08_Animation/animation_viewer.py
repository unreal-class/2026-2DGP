# Drill 08: AI를 이용한 애니메이션 뷰어
import json
from pico2d import *

WIDTH, HEIGHT = 800, 600
SCALE = 1
FRAME_TIME = 0.09
REPEATS = 5
PAUSE_TIME = 1.0
ANIMATIONS = [["idle","대기"],["run","달리기"],["attack_A","공격"],["die","쓰러짐"]]

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
all_frames = sorted(all_frames, key=lambda frame: frame['filename'])
while True:
    for key, name in ANIMATIONS:
        frames = [frame for frame in all_frames
                  if frame['filename'].startswith(key + '/')]
        for repeat in range(REPEATS):
            for frame in frames:
                draw_frame(sheet, frame)
                delay(FRAME_TIME)
        delay(PAUSE_TIME)
close_canvas()
