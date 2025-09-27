from wordcount import WordCount

class App: 
    def run(self):
        print("==== WORD COOUNTER ====")
        # Initial query analysis
        query = WordCount("best pizza best restaurant best service")
        query.word_counter()
        print(query.word_frequencies)


        # Changing query
        query.search_query = "grape mango grape"
        query.word_counter()
        print(analyzer.word_frequencies)

