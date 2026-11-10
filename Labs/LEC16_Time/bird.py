from pico2d import get_canvas_width, load_image

import game_framework


class Bird:
    """A single animated bird from the shared flight sprite sheet."""

    FRAME_WIDTH = 153
    FRAME_HEIGHT = 169
    FRAME_COUNT = 6

    def __init__(self, x, y, speed, direction=1):
        self.x = x
        self.y = y
        # Each instance owns its flight lane, pace, and heading.  This keeps
        # the ten birds from moving as one synchronized group.
        self.speed = speed
        self.direction = direction
        self.frame = 0.0
        self.image = load_image('bird_animation.png')

    def update(self):
        """Advance on the x axis and reverse at the visible canvas edges."""
        self.x += self.direction * self.speed * game_framework.frame_time

        half_width = self.FRAME_WIDTH // 2
        left_edge = half_width
        right_edge = get_canvas_width() - half_width
        if self.x <= left_edge:
            self.x = left_edge
            self.direction = 1
        elif self.x >= right_edge:
            self.x = right_edge
            self.direction = -1
