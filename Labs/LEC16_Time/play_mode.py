from pico2d import *
import game_world
import game_framework
from boy import Boy
from bird import Bird
from grass import Grass

boy = None
birds = []


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy, birds

    # Stagger lanes, speeds, positions, and headings so the flock looks like
    # separate birds sharing the same sky instead of one copied animation.
    flight_specs = [
        (120, 460, 110, 1), (340, 390, 145, -1),
        (560, 520, 125, 1), (780, 330, 165, -1),
        (1000, 450, 135, 1), (1220, 370, 155, -1),
        (1440, 500, 115, 1), (250, 290, 175, -1),
        (690, 240, 130, 1), (1160, 270, 150, -1),
    ]
    # A different phase prevents ten identical wing poses at startup.
    birds = [Bird(*spec, start_frame=index * 1.6)
             for index, spec in enumerate(flight_specs)]
    for bird in birds:
        game_world.add_oject(bird)

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, birds
    game_world.clear()
    boy = None
    birds = []


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









