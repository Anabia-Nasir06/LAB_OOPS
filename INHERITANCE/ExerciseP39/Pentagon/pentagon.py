from Regpolygon.regpolygon import RegularPolygon
class Pentagon(RegularPolygon):
    def __init__(self, side):
        super().__init__(5, side)