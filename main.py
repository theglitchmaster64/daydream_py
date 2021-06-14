#!/usr/bin/env python3

from engine.stuff import *
import sys, time, random
from sdl2 import SDL_QUIT
from engine.stuff import Colors

if __name__=='__main__':
    mgr = Manager(title='supm8', res=(640,480))
    mgr.start()
    while True:
        tmp_pt = Point(random.randint(0,640),random.randint(0,480),color=Colors().random())
        mgr.add_gameobject(tmp_pt)
        retcode = mgr.update_frame()
        if retcode == 'MGR_QUIT':
            break
    sys.exit(0)
