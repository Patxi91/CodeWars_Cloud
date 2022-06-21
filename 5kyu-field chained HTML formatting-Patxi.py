class Format:

    def __init__(self, tag='{}'):
        self.tag = tag

    def __call__(self, *args):
        return self.tag.format(''.join(args))

    def __getattr__(self, name):
        return Format(self.tag.format(f'<{name}>{"{}"}</{name}>'))


format = Format()
