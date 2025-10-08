from wordcount import WordCount

class App: 
    def run(self):
        print("\n==== WORD COOUNTER ====\n")
        # Initial query analysis
        query = WordCount("best pizza best restaurant best service")
        print(query)
        print("Word count:",query.word_counter(), "\n")


        # Changing query
        query.search_query = "buy phone buy charger"
        print(query)
        print("Word count:",query.word_counter())

