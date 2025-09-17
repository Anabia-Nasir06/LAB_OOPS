from wordcount import WordCount

class App: 
    def run(self):
        print("==== WORD COOUNTER ====")
        q = WordCount("apple orange apple banana apple orange")
        print("Word counts:", q.word_counter())