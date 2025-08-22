class Vector:
    def __init__(self, d: int):
        # Make a vector with d dimensions, all starting at zero.
        self._coordinates = [0] * d

    def __len__(self):
        # Return how many dimensions this vector has.
        return len(self._coordinates)

    def __getitem__(self, j: int):
        # Get the value at position j.
        return self._coordinates[j]

    def __setitem__(self, j: int, value):
        # Change the value at position j.
        self._coordinates[j] = value

    def __add__(self, other: "Vector"):
        # Add two vectors of the same dimension and return a new one.
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other: object):
        # Check if two vectors are exactly the same.
        if not isinstance(other, Vector):
            return NotImplemented
        return self._coordinates == other._coordinates

    def __ne__(self, other: object):
        # Check if two vectors are different.
        return not self == other

    def __str__(self):
        # Show the vector nicely, e.g., <1, 2, 3>.
        return "<" + str(self._coordinates)[1:-1] + ">"
