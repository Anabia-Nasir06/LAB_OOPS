class Point:
    count_obj = 0
    def __init__(self,x=0.0,y=0.0):
        if isinstance(x,Point):
            self._x = x.x
            self._y = x.y
        else:
            self._x = x
            self._y = y
        Point.count_obj+=1
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x = value
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self,value):
        self._y = value
    
    def __Str__(self):
        return f"{self._x},{self._y}"

    def __add__(self,other):
        if isinstance(other,Point):
            return self._x+other._x, self._y+other._y

    def distance(self,p):
        return ((self._x-p._x)**2+(self._y-p._y)**2)**0.5
    @classmethod
    def objcount(cls):
        return cls.count_obj