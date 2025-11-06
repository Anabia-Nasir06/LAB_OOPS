from Regpolygon.regpolygon import RegularPolygon
class Hexagon(RegularPolygon):
    def __init__(self, side):
        super().__init__(6, side)