from pico2d import *
import os

# VS Code에서 어느 폴더를 열어도 이미지 파일을 찾을 수 있도록 합니다.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

while running:
    for action in (3, 2, 1, 0):
        frame = 0
        for repeat in range(5):
            for count in range(8):
                handle_events()
                if not running:
                    break

                clear_canvas()
                grass.draw(400, 30)
                character.clip_draw(
                    frame * 100, action * 100,
                    100, 100, 400, 300, 500, 500
                )
                update_canvas()

                frame = (frame + 1) % 8
                delay(0.05)

            if not running:
                break

        if not running:
            break

        # 마지막 프레임에서 총 1초 정지합니다.
        # 정지 중에도 창 닫기와 ESC를 처리합니다.
        for count in range(20):
            handle_events()
            if not running:
                break
            delay(0.05)

        if not running:
            break

close_canvas()
