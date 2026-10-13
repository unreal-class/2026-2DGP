from pico2d import *
import random
from pathlib import Path
from time import perf_counter


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

    def update(self, frame_time):
        # 바닥을 지나쳐도 반지름만큼 위에서 정확히 멈춘다.
        self.y = max(GROUND_Y + self.radius,
                     self.y - self.speed * frame_time)

    def draw(self):
        self.image.draw(self.x, self.y)


class Grass:
    def __init__(self):
        self.image = load_image(str(ASSET_DIR / 'grass.png'))

    def draw(self):
        self.image.draw(WIDTH / 2, GROUND_Y / 2)

    def update(self):
        pass


def reset_world():
    global running, grass, balls
    running = True
    grass = Grass()
    sizes = [21, 41] * (BALL_COUNT // 2)
    random.shuffle(sizes)
    # 중복 없이 뽑아 모든 공의 낙하 속도를 다르게 한다.
    # 초당 픽셀 단위 속도: 프레임 수와 무관하게 일정하게 떨어진다.
    speeds = random.sample(range(80, 301), BALL_COUNT)
    balls = [Ball(size, speed) for size, speed in zip(sizes, speeds)]


def update_world(frame_time):
    grass.update()
    for ball in balls:
        ball.update(frame_time)


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
        render_world()
        previous_time = perf_counter()
        while running:
            handle_events()
            if not running:
                break
            current_time = perf_counter()
            frame_time = current_time - previous_time
            previous_time = current_time
            update_world(frame_time)
            render_world()
            delay(0.01)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
