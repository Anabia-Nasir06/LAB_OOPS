from polygon import Polygon
import math
class RegularPolygon(Polygon):
    def __init__(self,n,side):
        self.n = n
        self.side = side
    def area(self):
         return (self.n * self.side**2) / (4 * math.tan(math.pi / self.n))
    def perimeter(self):
        return self.n*self.side