from Hexagon.hexagon import Hexagon
from Pentagon.pentagon import Pentagon
from Quad.quadrilateral import Quadrilaterals
from Quad.rectangle import Rectangle
from Quad.square import Square
from Regpolygon.regpolygon import RegularPolygon
from Triangle.triangle import Triangle
from Triangle.equilateral import Equilaterel
from Triangle.isoceles import Isoceles
from Octagon.octagon import Octagon

def App():
    print("Choose shape: \n"
          "1 = Triangle\n"
          "2 = Rectangle\n"
          "3 = Square\n"
          "4 = Equilateral Triangle\n"
          "5 = Pentagon\n"
          "6 = Hexagon\n"
          "7 = Octagon")
    
    choice = int(input("Enter choice: "))

    match choice:
        case 1:
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))
            shape = Triangle(side1, side2, side3)

        case 2:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            shape = Rectangle(length, width)

        case 3:
            side = float(input("Enter side: "))
            shape = Square(side)

        case 4:
            side1 = float(input("Enter side 1: "))
            side2 = float(input("Enter side 2: "))
            side3 = float(input("Enter side 3: "))
            shape = Equilaterel(side1, side2, side3)

        case 5:
            side = float(input("Enter side: "))
            shape = Pentagon(side)

        case 6:
            side = float(input("Enter side: "))
            shape = Hexagon(side)

        case 7:
            side = float(input("Enter side: "))
            shape = Octagon(side)

        case _:  # default case
            print("Invalid choice")
            return

    print(f"Perimeter = {shape.perimeter():.2f}")
    print(f"Area = {shape.area():.2f}")
