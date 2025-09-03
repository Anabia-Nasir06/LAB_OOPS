from point import Point
from line import Line
import tkinter as tk

class MyCanvas(tk.Canvas):
    def __init__(self, master=None, width=400, height=400, **kwargs):
        super().__init__(master, width=width, height=height, bg='white', **kwargs)
        self.lines = []

    def add_line(self, p1: Point, p2: Point):
        """Add a line to the canvas"""
        self.lines.append(Line(p1, p2))
        print(f"Line from ({p1.x}, {p1.y}) → ({p2.x}, {p2.y})")
        self.draw()

    def draw(self):
        """Draw all stored lines"""
        self.delete("all")
        for line in self.lines:
            self.create_line(line.start.x, line.start.y,
                             line.end.x, line.end.y,
                             fill='black', width=2)
