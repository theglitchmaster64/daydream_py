#!/usr/bin/env python3

from engine.stuff import *
import sys, time, random
from sdl2 import SDL_QUIT
from engine.stuff import Colors

if __name__=='__main__':
    mgr = Manager(title='supm8', res=(640,480),renlim=32)
    mgr.start()
    r = 1
    while True:
        mgr.add_gameobject(Circle(320,240,r%240,color=Colors().new_color(), persist=True))
        r += 5
        retcode = mgr.update_frame()
        print(len(mgr.render_list))
        if retcode == 'MGR_QUIT':
            break
    sys.exit(0)
