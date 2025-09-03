import tkinter as tk
from point import Point
from line import Line
from pen import Pen
from canvas import MyCanvas
from Turtle import TurtleApp
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Muse")
        self.canvas = MyCanvas(self.root,width=400,height=400)
        self.canvas.pack()
        self.app = TurtleApp(self.canvas)

    def run(self):
        commands = input("Enteer The Command \n")
        self.app.run(commands)
        self.root.mainloop()