class WordCount:
    def __init__(self, text):
        self.text = text

    def word_counter(self):
        words = self.text.split()
        counts = {}
        for w in words:
            counts[w] = counts.get(w, 0) + 1
        return counts