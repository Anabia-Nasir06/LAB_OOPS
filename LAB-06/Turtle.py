from pen import Pen
class TurtleApp:
    def __init__(self, canvas):
        self.pen = Pen(canvas)

    def run(self, commands):
        for cmd in commands:
            if cmd == "F":
                self.pen.forward()
            elif cmd == "+":
                self.pen.turn_right(90)
            elif cmd == "-":
                self.pen.turn_left(90)