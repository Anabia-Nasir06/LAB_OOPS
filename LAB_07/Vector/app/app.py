# app/app.py
from vector import Vector  # file ka naam vector.py ho

class App:
    def __init__(self):
        # No assignment values needed
        pass

    def run(self):
        A = Vector(3)
        B = Vector(3)
        C = Vector(4)
        D = Vector(4)
        E = Vector(5)

        print("The number of dimensions of vector A are:")
        print(len(A), "\n")

        # Equality
        print("Do Vectors A", A, "and B", B, "have the same coordinates ?")
        print(A.__eq__(B), "\n")  

        print("Original coordinates of vector C:""\n",C, "\n")

        # Setting coordinates of vector C.__setitem__()
        print("Setting coordinates of dimensions of vector C as 10 , 8 , 5, 6 respectively")
        C[0] = 10 
        C[1] = 8 
        C[2] = 5  
        C[3] = 6  

        # Return coordinates of vector C.__getitem__(0)
        print("Displaying new coordinates of Vector C:")
        print(C[0],",", C[1],",", C[2],",", C[3], "\n")            
       

        # Checking inequality of vectors C.__ne__(D)
        print("Do Vectors C", C, "and D", D, "not have the same coordinates ?")
        print(C != D, "\n")  

        # Testing addition functionality of Vectors
        D[0] = 11
        D[1] = 21
        D[2] = 31
        D[3] = 41

        F = C + D              # C.__add__(D)
        print("Addition of Vectors C", C, "and D", D, "equals to:")
        print(F, "\n")

        # Displaying Vector attributes as String
        print("Coordinates of Vector E as string:")
        print(E, "\n")   # E.__str__()
