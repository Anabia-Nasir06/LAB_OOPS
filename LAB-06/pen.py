from point import Point
import math
class Pen:
    def __init__(self,canvas):
        self._canvas = canvas
        self._cp = Point(200,200)
        self._angle = 0 
    def moveto(self,x,y):
        self._cp = Point(x,y)
    def lineto(self,x,y):
        new_point = Point(x,y)
        self._canvas.add_line(self._cp,new_point)
        self._cp = new_point
    def forward(self, distance=50):
        # calculate new point using angle
        rad = math.radians(self._angle)
        new_x = self._cp.x + distance * math.cos(rad)
        new_y = self._cp.y - distance * math.sin(rad)  # minus because tkinter y goes down
        self.lineto(new_x, new_y)

    def turn_right(self, angle=90):
        self._angle -= angle

    def turn_left(self, angle=90):
        self._angle += angle
    def getposition(self):
        return self._cp
