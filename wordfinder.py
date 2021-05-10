"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        """Creates new WordFinder instance with given path to words.txt."""
        self.path = path
        words_file = open(path)
        self.words_list = self.make_words_list(words_file)

        print(f"{len(self.words_list)} words read")

    def make_words_list(self, words_file):
        return [w.strip() for w in words_file]

    def random_word(self):
        return random.choice(self.words_list)


class SpecialWordFinder(WordFinder):
    def __init__(self, path)
        super().__init__(path)

    def remove_empty_lines_hashtags(self):
        return [w.strip() for w in words_file if w.strip() != "" and not w.startswith('#')]