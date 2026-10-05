import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png') 

cx, cy = 400, 300   
radius = 150        
angle = 0.0         
speed = 2.0        

running = True
while running:
    clear_canvas()

    angle += speed
    
    rad = math.radians(angle)

    x = cx + radius * math.cos(rad)
    y = cy + radius * math.sin(rad)

    character.draw(x, y)

    update_canvas()

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    delay(0.01)

close_canvas()