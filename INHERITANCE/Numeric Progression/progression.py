class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self.current = start

    def advance(self):
        """Update self.current to a new value."""
        self.current += 1

    def next(self):
        """Return the next element, or else raise StopIteration error."""
        if self.current is None:
            raise StopIteration()
        else:
            answer = self.current
            self.advance()
            return answer

    def iter(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(self.next()) for j in range(n)))
