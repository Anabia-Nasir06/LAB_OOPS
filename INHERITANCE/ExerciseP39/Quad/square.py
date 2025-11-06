from Quad.quadrilateral import Quadrilaterals
class Square(Quadrilaterals):
    def __init__(self, sides):
        super().__init__(sides)
        self.sides = sides
    def area(self):
        return (self.sides)**2
    def perimeter(self):
        return 4*self.sides
        