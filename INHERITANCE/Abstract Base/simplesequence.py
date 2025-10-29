from sequence import Sequence

# Concrete class implementing the abstract methods of Sequence
class SimpleSequence(Sequence):
    def __init__(self, data):
        self._data = list(data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, j):
        return self._data[j]


