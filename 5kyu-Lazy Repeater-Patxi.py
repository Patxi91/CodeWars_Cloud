class make_looper:
    def __init__(self, s):
        self.s = s
        self.i = -1

    def __call__(self):
        self.i += 1
        return self.s[self.i % len(self.s)]
