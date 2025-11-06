from polygon import Polygon
class Quadrilaterals(Polygon):
    def __init__(self,sides):
        self.sides = sides
    def area(self):
        pass
    def perimeter(self):
        return sum(self.sides)