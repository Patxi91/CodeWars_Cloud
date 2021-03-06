class SecureList:

    def __init__(self, lst):
        self.data = lst.copy()

    def __getitem__(self, attr):
        return self.data.pop(attr)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        result, self.data = self.data, []
        return str(result)

    def __str__(self):
        result, self.data = self.data, []
        return str(result)
