from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

# fill here
character.clip_composite_draw(
                frame * 100, 0, # left, bottom
                100, 100, # right, top
                0, 'h',
                x, 90, # right, top
                200, 200 # width, height
            )

close_canvas()

    