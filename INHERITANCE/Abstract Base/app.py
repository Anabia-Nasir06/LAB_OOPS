from sequence import Sequence
from simplesequence import SimpleSequence

class App:
    def run(self):
        seq = SimpleSequence([10, 20, 30, 20, 40, 20])

        print("Sequence:", seq._data)
        print("Length:", len(seq))
        print("Element at index 2:", seq[2])
        print("Does it contain 30?", 30 in seq)
        print("Does it contain 50?", 50 in seq)
        print("Index of first 20:", seq.index(20))
        print("Count of 20:", seq.count(20))
