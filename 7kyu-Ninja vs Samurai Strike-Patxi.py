class Warrior:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def strike(self, enemy: 'Warrior', *args):
        for arg in args:
            if isinstance(arg, int):
                swings = arg
        # health cannot go below zero
        enemy.health = max([0, enemy.health - (swings * 10)])
