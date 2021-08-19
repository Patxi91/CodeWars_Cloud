class Vector:
    def __init__(self, values):
        self.values = values

    def add(self, b):
        if len(self.values) != len(b.values):
            raise Exception
        res = []
        for (item1, item2) in zip(self.values, b.values):
            res.append(item1+item2)
        return Vector(res)

    def subtract(self, b):
        if len(self.values) != len(b.values):
            raise Exception
        res = []
        for (item1, item2) in zip(self.values, b.values):
            res.append(item1 - item2)
        return Vector(res)

    def dot(self, b):
        res = 0
        for (item1, item2) in zip(self.values, b.values):
            res += item1 * item2
        return res

    def norm(self):
        return sum([item**2 for item in self.values])**0.5

    def __str__(self):
        return f'({str(self.values)[1:-1]})'.replace(' ', '')

    def equals(self, b):
        return set(self.values) == set(b.values)

