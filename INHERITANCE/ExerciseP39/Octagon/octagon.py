from Regpolygon.regpolygon import RegularPolygon
class Octagon(RegularPolygon):
    def __init__(self, side):
        super().__init__(8, side)