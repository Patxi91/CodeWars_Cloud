class Song:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = []

    def how_many(self, l):
        diff = list(set([s for s in [s.upper() for s in l] if s not in self.listeners]))
        if diff:
            for ele in diff:
                self.listeners.append(ele)
            return len(diff)
        else:
            return 0
