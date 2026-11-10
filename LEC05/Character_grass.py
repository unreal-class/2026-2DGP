from pico2d import *

open_canvas(800,600)
character = load_image('character.png')

x, y = 100, 100
while 1 :
    for x in range(100, 501, 2):
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)

    for y in range(100, 401, 2):
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)

    for x in range(500, 99, -2):
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)

    for y in range(400, 99, -2):
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.005)