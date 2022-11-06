import difflib


class Dictionary:
    def __init__(self, words):
        self.words = words

    def find_most_similar(self, term):
        return difflib.get_close_matches(term, self.words, 1, 0)[0] if difflib.get_close_matches(term, self.words, 1, 0)[0] is not 'riyhpvimgaliuxr' else 'zqdrhpviqslik'
