#!/usr/bin/env python3

from engine.stuff import test
import sdl2.ext as sdl
from sdl2 import SDL_QUIT
import time, random

RED = sdl.Color(255,0,0)
GREEN = sdl.Color(0,255,0)
BLUE = sdl.Color(0,0,255)
BLACK = sdl.Color(0,0,0)
WHITE = sdl.Color(255,255,255)

colors = [RED,GREEN,BLUE,WHITE,BLACK]

def main_loop():
    sdl.init()
    window = sdl.Window('supm8',size=(640,480))
    rend = sdl.Renderer(window)
    window.show()
    running = True
    i = 0
    while running:
        i = (i + 1) % 5
        rend.clear(colors[i])
        rend.present()
        events = sdl.get_events()
        for e in events:
            if e.type == SDL_QUIT:
                running = False
                break
    return 0

if __name__=='__main__':
    test()
    main_loop()
