class WordCounter:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = self.count_words()

    def count_words(self):
        return self.sentence.split()

    def get_word_count(self):
        return len(self.words)

    def get_shortest_word(self):
        letters = len(self.words[0].split())

        for word in self.words:
            if len(word) < letters:
                letters = len(word)
        return letters

    def get_longest_word(self):
        letters = 0

        for word in self.words:
            if len(word) > letters:
                letters = len(word)
        return letters
