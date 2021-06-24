#!/usr/bin/env python3

from engine.stuff import *
import sys, time, random
from sdl2 import SDL_QUIT
from engine.stuff import Colors

if __name__=='__main__':
    mgr = Manager(title='supm8', res=(1920,1080),renlim=16)
    mgr.start()
    r = 1
    p = 329
    q = 239
    s = 1
    while True:
        t1 = time.time()
        #mgr.add_gameobject(Circle(random.randint(0,1920),random.randint(0,1080),random.randint(1,240),color=Colors().new_color()))
        mgr.add_gameobject(Circle(1920//2, 1080//2, r%320, color=Colors().new_color(bias_low=(32,64,32), bias_up=(64,255,64))))
        mgr.add_gameobject(Circle(1920//2, 1080//2, p%320, color=Colors().new_color(bias_low=(64,32,64), bias_up=(255,64,255))))
        mgr.add_gameobject(Circle(1920//2, 1080//2, q%240, color=Colors().new_color(bias_low=(64,32,32), bias_up=(255,64,64))))
        mgr.add_gameobject(Circle(1920//2, 1080//2, s%240, color=Colors().new_color(bias_low=(32,32,64), bias_up=(64,64,255))))
        #mgr.add_gameobject(Point(random.randint(0,1920), random.randint(0,1080), color=Colors().new_color()))
        r += 2
        p -= 2
        q -= 4
        s += 4
        retcode = mgr.update_frame()
        elapsed = time.time() - t1
        print('fps:',1/elapsed)
        if retcode == 'MGR_QUIT':
            break
    sys.exit(0)
