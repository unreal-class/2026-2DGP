from pico2d import get_canvas_width, load_image

import game_framework


class Bird:
    """A single animated bird from the shared flight sprite sheet."""

    # Source is 918 x 506: five poses in each of the first two rows,
    # four in the last. Beaks repeat every 182 pixels, not 153 pixels.
    # Explicit (left, bottom, width, height) rectangles in pico2d coordinates.
    FRAME_RECTS = (
        (0, 337, 182, 169), (182, 337, 182, 169),
        (364, 337, 182, 169), (546, 337, 182, 169),
        (728, 337, 182, 169),
        (0, 168, 182, 169), (182, 168, 182, 169),
        (364, 168, 182, 169), (546, 168, 182, 169),
        (728, 168, 182, 169),
        # Exclude the preceding row's wing tip above the final row.
        (0, 0, 182, 160), (182, 0, 182, 160),
        (364, 0, 182, 160), (546, 0, 182, 160),
    )
    FRAME_COUNT = len(FRAME_RECTS)
    DRAW_WIDTH = 122
    DRAW_HEIGHT = 113
    FLAP_FRAMES_PER_SECOND = 10

    def __init__(self, x, y, speed, direction=1, start_frame=0.0):
        self.x = x
        self.y = y
        # Each instance owns its flight lane, pace, and heading.  This keeps
        # the ten birds from moving as one synchronized group.
        self.speed = speed
        self.direction = direction
        self.frame = start_frame % self.FRAME_COUNT
        self.image = load_image('bird_animation.png')

    def update(self):
        """Advance on the x axis and reverse at the visible canvas edges."""
        self.x += self.direction * self.speed * game_framework.frame_time
        self.frame = (self.frame + self.FLAP_FRAMES_PER_SECOND *
                      game_framework.frame_time) % self.FRAME_COUNT

        half_width = self.DRAW_WIDTH // 2
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
        rect = self.FRAME_RECTS[int(self.frame)]
        height = self.DRAW_HEIGHT * rect[3] / 169
        center_y = self.y - (self.DRAW_HEIGHT - height) / 2
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            *rect,
            0, flip, self.x, center_y, self.DRAW_WIDTH, height
        )
