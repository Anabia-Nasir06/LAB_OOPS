class WordCount:
    def __init__(self, search_query):
        self._search_query = search_query
        self._word_list = self._search_query.split()
        self._unique_words = []
        self._word_frequencies = []

    @property
    def search_query(self):
        return self._search_query

    @search_query.setter
    def search_query(self, value):
        self._search_query = value
        self._word_list = self._search_query.split()
        self._unique_words = []
        self._word_frequencies = []

    def word_counter(self):
        for word in self._word_list:
            if word in self._unique_words:
                index = self._unique_words.index(word)
                self._word_frequencies[index] += 1
            else:
                self._unique_words.append(word)
                self._word_frequencies.append(1)

    @property
    def word_frequencies(self):
        return [[self._unique_words[i], self._word_frequencies[i]] for i in range(len(self._unique_words))]

    def __str__(self):
        return f"SearchQueryAnalyzer(search_query='{self._search_query}')"