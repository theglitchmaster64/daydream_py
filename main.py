#!/usr/bin/env python3

from engine.stuff import *
import sys, time, random
from sdl2 import SDL_QUIT
from engine.stuff import Colors

if __name__=='__main__':
    mgr = Manager(title='supm8', res=(640,480))
    mgr.start()
    while True:
        t1 = time.time()
        #mgr.add_gameobject(Point(random.randint(0,640),random.randint(0,480),Colors().new_color()))
        mgr.add_gameobject(Circle(320,240,120,color=Colors().new_color(), persist=False))
        retcode = mgr.update_frame()
        elapsed = time.time() - t1
        t1 = time.time()
        print('fps=',1/elapsed)
        if retcode == 'MGR_QUIT':
            break
    sys.exit(0)
