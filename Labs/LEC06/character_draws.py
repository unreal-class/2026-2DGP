# 실습 과제 진행 - AI 도움을 받아 단계별로 작성
from pico2d import *


open_canvas(800, 600)
boy = load_image('character.png')
clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)
close_canvas()
