from Quad.quadrilateral import Quadrilaterals
class Rectangle(Quadrilaterals):
    def __init__(self, length,width):
        super().__init__([length,width,length,width])
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width