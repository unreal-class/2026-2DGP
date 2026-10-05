from pico2d import *


open_canvas(800, 600)

# 여기를 채우시오.
grass = load_image('grass.png')
character = load_image('character.png')

grass.draw(400, 30)
character.draw(400, 90)




update_canvas()
delay(2)

close_canvas()

