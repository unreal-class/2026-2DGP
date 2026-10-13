from pico2d import *
import random
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parent
WIDTH, HEIGHT = 800, 600
BALL_COUNT = 20


class Ball:
    def __init__(self, size):
        self.image = load_image(str(ASSET_DIR / f'ball{size}x{size}.png'))
        self.radius = size / 2
        self.x = random.randint(size // 2 + 1, WIDTH - size // 2 - 1)
        self.y = 599

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image(str(ASSET_DIR / 'grass.png'))

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


def reset_world():
    global running, grass, balls
    running = True
    grass = Grass()
    sizes = [21, 41] * (BALL_COUNT // 2)
    random.shuffle(sizes)
    balls = [Ball(size) for size in sizes]


def update_world():
    grass.update()


def render_world():
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
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
