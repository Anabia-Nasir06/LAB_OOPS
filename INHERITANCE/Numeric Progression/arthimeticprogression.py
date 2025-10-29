from progression import Progression 

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression."""
        super().__init__(start)
        self.increment = increment

    def advance(self):
        """Update current value by adding the fixed increment."""
        self.current += self.increment
