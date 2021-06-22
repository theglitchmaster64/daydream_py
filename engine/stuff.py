import sdl2.ext as sdl
from sdl2 import SDL_QUIT
import random
import math

RED = sdl.Color(255,0,0)
GREEN = sdl.Color(0,255,0)
BLUE = sdl.Color(0,0,255)
BLACK = sdl.Color(0,0,0)
WHITE = sdl.Color(255,255,255)

def dist(p1,p2):
    return math.sqrt( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )

class Colors:
    def __init__(self):
        self.color_list = [RED,GREEN,BLUE,WHITE,BLACK]

    def random(self,type='all'):
        if type == 'fg':
            selection = random.randint(0,2)
        elif type == 'bg':
            selection = random.randint(3,4)
        elif type == 'all':
            selection = random.randint(0,4)
        return self.color_list[selection]

    def new_color(self):
        return sdl.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))


def test():
    print('ok')

class Manager:
    def __init__(self,title, res, back_color = BLACK, fore_color = WHITE):
        self.render_list = []
        self.bg_color = back_color
        self.fg_color = fore_color
        self.window = sdl.Window(title,size=res)
        self.renderer = sdl.Renderer(self.window)
        sdl.init()

    def start(self):
        self.window.show()

    def update_frame(self):
        self.renderer.clear(self.bg_color)
        for item in self.render_list:
            if item.rend == None:
                item.set_renderer(self.renderer)
            self.renderer.color = item.color
            item.draw()
            if item.persist == False:
                self.render_list.remove(item)
        self.renderer.present()
        events = sdl.get_events()
        for e in events:
            if e.type == SDL_QUIT:
                return 'MGR_QUIT'

    def set_bgcolor(color):
        self.bg_color = color

    def set_fgcolor(color):
        self.fg_color = color

    def add_gameobject(self,gameobject):
        self.render_list.append(gameobject)

class Point:
    def __init__(self, x, y, color, persist = True):
        self.x = x
        self.y = y
        self.rend = None
        self.color = color
        self.persist = persist

    def set_renderer(self,renderer):
        self.rend = renderer

    def draw(self):
        if self.rend == None:
            return False
        else:
            self.rend.draw_point(points = [self.x,self.y])

    def set_color(self,color):
        self.color = color
        self.rend.color = self.color

    def set_pos(self, x, y):
        self.x = x
        self.y = y

class Rect:
    def __init__(self,x1,y1,x2,y2,color = GREEN, persist = True):
        self.x = x1
        self.y = y1
        self.w = abs(x1-x2)
        self.h = abs(y1-y2)
        self.color = color
        self.persist = persist


class Circle:
    def __init__(self, x, y, r, color = GREEN, persist = True):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.persist = persist
        self.rend = None

    def set_renderer(self, renderer):
        self.rend = renderer

    def set_color(self, color):
        self.color = color
        self.rend.color = self.color

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def _draw_helper(self,xc,yc,h,k):
        self.rend.draw_point([xc+h,yc+k])
        self.rend.draw_point([xc-h,yc-k])
        self.rend.draw_point([xc+h,yc-k])
        self.rend.draw_point([xc-h,yc+k])
        self.rend.draw_point([xc+k,yc+h])
        self.rend.draw_point([xc-k,yc-h])
        self.rend.draw_point([xc+k,yc-h])
        self.rend.draw_point([xc-k,yc+h])



    def draw(self):
        x0 = 0
        r0 = self.r
        d = 3 - 2*r0
        self._draw_helper(self.x, self.y, x0, r0)
        while (r0 >= x0):
            x0 += 1
            if (d > 0):
                r0 -= 1
                d = d + (4 * (x0 - r0)) + 10
            else:
                d = d + (4*x0) + 6
                self._draw_helper(self.x, self.y, x0, r0)
