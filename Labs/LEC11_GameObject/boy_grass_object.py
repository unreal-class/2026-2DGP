from pathlib import Path
import random

from pico2d import *


ASSET_DIR = Path(__file__).resolve().parent


class Grass:
    def __init__(self):
        self.image = load_image(str(ASSET_DIR / 'grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 90
        self.frame = random.randint(0, 7)
        self.image = load_image(str(ASSET_DIR / 'run_animation.png'))

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global world
    world = [Grass()]
    world += [Boy() for _ in range(10)]


def update_world():
    for obj in world:
        obj.update()


def render_world():
    clear_canvas()
    for obj in world:
        obj.draw()
    update_canvas()


def main():
    global running
    running = True
    open_canvas()
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
