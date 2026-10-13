from pico2d import *
import random
from pathlib import Path


ASSET_DIR = Path(__file__).resolve().parent
WIDTH, HEIGHT = 800, 600
BALL_COUNT = 20
GROUND_Y = 60


class Ball:
    def __init__(self, size, speed):
        self.image = load_image(str(ASSET_DIR / f'ball{size}x{size}.png'))
        self.radius = size / 2
        self.x = random.randint(size // 2 + 1, WIDTH - size // 2 - 1)
        self.y = 599
        self.speed = speed

    def update(self):
        # 바닥을 지나쳐도 반지름만큼 위에서 정확히 멈춘다.
        self.y = max(GROUND_Y + self.radius, self.y - self.speed)

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
    # 중복 없이 뽑아 모든 공의 낙하 속도를 다르게 한다.
    speeds = random.sample(range(2, 32), BALL_COUNT)
    balls = [Ball(size, speed) for size, speed in zip(sizes, speeds)]


def update_world():
    grass.update()
    for ball in balls:
        ball.update()


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
