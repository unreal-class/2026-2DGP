# Drill 08: AI를 이용한 애니메이션 뷰어
import json
from time import perf_counter
from pico2d import *

WIDTH, HEIGHT = 800, 600
SCALE = 8
FRAME_TIME = 0.09
REPEATS = 5
PAUSE_TIME = 1.0
ANIMATIONS = [["idle","대기"],["run","달리기"],["attack_A","공격"],["die","쓰러짐"]]

def wait(seconds):
    end = perf_counter() + seconds
    while perf_counter() < end:
        for event in get_events():
            if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                close_canvas()
                raise SystemExit
        delay(min(0.01, max(0, end - perf_counter())))


def draw_frame(sheet, frame, font, text):
    box = frame['frame']
    w, h = box['w'], box['h']
    x, y = WIDTH / 2, HEIGHT / 2
    # 잘려 나간 투명 여백의 위치를 복원해 중심이 흔들리지 않게 한다.
    trim = frame['spriteSourceSize']
    source = frame['sourceSize']
    x += (trim['x'] + w / 2 - source['w'] / 2) * SCALE
    y += (source['h'] / 2 - trim['y'] - h / 2) * SCALE
    clear_canvas()
    # JSON은 위에서부터, pico2d는 아래에서부터 y 좌표를 센다.
    sheet.clip_draw(box['x'], sheet.h - box['y'] - h, w, h,
                    x, y, w * SCALE, h * SCALE)
    font.draw(24, HEIGHT - 28, 'ANIMATION VIEWER', (35, 35, 45))
    font.draw(24, 24, text, (35, 35, 45))
    font.draw(WIDTH - 112, 24, 'ESC 종료', (70, 70, 80))
    update_canvas()


open_canvas(WIDTH, HEIGHT)
sheet = load_image('viewer_knight.png')
with open('viewer_knight.json', encoding='utf-8') as file:
    data = json.load(file)
all_frames = data['textures'][0]['frames']
all_frames = sorted(all_frames, key=lambda frame: frame['filename'])
font = load_font('C:/Windows/Fonts/malgun.ttf', 20)
while True:
    for key, name in ANIMATIONS:
        frames = [frame for frame in all_frames
                  if frame['filename'].startswith(key + '/')]
        for repeat in range(REPEATS):
            for frame in frames:
                text = f'{name} | {len(frames)}프레임 | {repeat + 1}/{REPEATS}회'
                draw_frame(sheet, frame, font, text)
                wait(FRAME_TIME)
        draw_frame(sheet, frames[-1], font,
                   f'{name} | {REPEATS}/{REPEATS}회 완료 - 1초 정지')
        wait(PAUSE_TIME)
close_canvas()
