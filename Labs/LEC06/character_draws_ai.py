from pathlib import Path
import math

from pico2d import *

canvas_width = 800
canvas_height = 600
center_x = canvas_width / 2
center_y = canvas_height / 2
asset_folder = Path(__file__).resolve().parent

open_canvas(canvas_width, canvas_height)
grass = load_image(str(asset_folder / 'grass.png'))
character = load_image(str(asset_folder / 'character.png'))


def draw_frame(position):
    clear_canvas()
    grass.draw(canvas_width / 2, 30)
    character.draw(position[0], position[1])
    update_canvas()
    delay(0.008)


def circle_path():
    radius = 180
    start_angle = math.pi / 2
    for step in range(361):
        angle = start_angle + math.tau * step / 360
        yield (
            center_x + radius * math.cos(angle),
            center_y + radius * math.sin(angle),
        )


def line_path(start, end, steps=90):
    for step in range(steps + 1):
        progress = step / steps
        x = start[0] + (end[0] - start[0]) * progress
        y = start[1] + (end[1] - start[1]) * progress
        yield (x, y)


def rectangle_path():
    corners = (
        (400, 480),
        (600, 480),
        (600, 120),
        (200, 120),
        (200, 480),
        (400, 480),
    )
    for start, end in zip(corners, corners[1:]):
        yield from line_path(start, end)


def triangle_path():
    corners = (
        (400, 480),
        (600, 120),
        (200, 120),
        (400, 480),
    )
    for start, end in zip(corners, corners[1:]):
        yield from line_path(start, end)


while True:
    for path in (circle_path, rectangle_path, triangle_path):
        for position in path():
            draw_frame(position)

close_canvas()
