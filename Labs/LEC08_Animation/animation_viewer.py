# Drill 08: AI를 이용한 애니메이션 뷰어
import json
from pico2d import *

WIDTH, HEIGHT = 800, 600

open_canvas(WIDTH, HEIGHT)
sheet = load_image('viewer_knight.png')
with open('viewer_knight.json', encoding='utf-8') as file:
    data = json.load(file)
all_frames = data['textures'][0]['frames']
delay(0.2)
close_canvas()
