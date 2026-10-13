from pico2d import *
import random
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parent
WIDTH, HEIGHT = 800, 600


class Grass:
    def __init__(self):
        self.image = load_image(str(ASSET_DIR / 'grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


def reset_world():
    global running, grass
    running = True
    grass = Grass()


def update_world():
    grass.update()


def render_world():
    clear_canvas()
    grass.draw()
    update_canvas()


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def main():
    open_canvas(WIDTH, HEIGHT)
    try:
        reset_world()
        while running:
            handle_events()
            update_world()
            render_world()
            delay(0.05)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
