# AI로 만든 원·사각·삼각 이동 예제
from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')
clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(0.1)
close_canvas()
