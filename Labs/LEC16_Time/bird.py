from pico2d import get_canvas_width, load_image

import game_framework


class Bird:
    """A single animated bird from the shared flight sprite sheet."""

    FRAME_WIDTH = 153
    FRAME_HEIGHT = 169
    FRAME_COUNT = 6
    FLAP_FRAMES_PER_SECOND = 10

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
        self.frame = (self.frame + self.FLAP_FRAMES_PER_SECOND *
                      game_framework.frame_time) % self.FRAME_COUNT

        half_width = self.FRAME_WIDTH // 2
        left_edge = half_width
        right_edge = get_canvas_width() - half_width
        if self.x <= left_edge:
            self.x = left_edge
            self.direction = 1
        elif self.x >= right_edge:
            self.x = right_edge
            self.direction = -1

    def draw(self):
        """Draw the current wing pose, mirroring it for leftward flight."""
        frame_x = int(self.frame) * self.FRAME_WIDTH
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            frame_x, 337, self.FRAME_WIDTH, self.FRAME_HEIGHT,
            0, flip, self.x, self.y, 122, 135
        )
