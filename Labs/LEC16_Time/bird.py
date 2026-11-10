from pico2d import load_image


class Bird:
    """A single animated bird from the shared flight sprite sheet."""

    FRAME_WIDTH = 153
    FRAME_HEIGHT = 169
    FRAME_COUNT = 6

    def __init__(self, x, y, speed, direction=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.frame = 0.0
        self.image = load_image('bird_animation.png')
