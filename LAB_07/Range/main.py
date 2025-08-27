from range import Range
if __name__ == "__main__":
        r1 = Range(10)
        r2 = Range(2, 10, 2)
        r3 = Range(10, 2, -2)

        print("r1 =", list(r1))
        print("r2 =", list(r2))
        print("r3 =", list(r3))

        print("Length of r2:", len(r2))
    
        print("Get Value From Index 1 of r2:", r2[1])
        print("Get Value From Index -1 of r2:", r2[-1])