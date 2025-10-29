from progression import Progression 

class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression."""
        super().__init__(start)
        self.base = base

    def advance(self):
        """Update current value by multiplying it by the base value."""
        self.current *= self.base
