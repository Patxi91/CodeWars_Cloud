
class Warrior:

    ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self.level = 1 # Max = 100
        self.rank = self.ranks[0]
        self.experience = 100
        self.achievements = []

    def add_exp(self, experience):
        if self.level < 100:
            self.experience += experience
            self.level = self.experience // 100
            if self.level >= 100:
                self.level = 100
                self.experience = 10000
            if self.rank != "Greatest":
                self.rank = self.ranks[self.level // 10]

    def battle(self, enemy_level):
        message = self.message(enemy_level)  # before battle
        if not 1 <= enemy_level <= 100:
            return "Invalid level"
        if self.level == enemy_level:
            earned_exp = 10
        elif self.level == enemy_level + 1:
            earned_exp = 5
        elif self.level > enemy_level + 1:
            earned_exp = 0
        elif enemy_level > self.level + 4 and (self.ranks.index(self.rank) < self.ranks.index(self.ranks[enemy_level // 10])):
            return "You've been defeated"
        else:  # Higher level enemy
            diff = enemy_level - self.level
            earned_exp = 20 * diff * diff
        self.add_exp(earned_exp)
        return message

    def message(self, enemy_level):
        if self.level >= enemy_level + 2:
            return "Easy fight"
        elif self.level == enemy_level + 1 or self.level == enemy_level:
            return "A good fight"
        else:  # self.level < enemy_level
            return "An intense fight"

    def training(self, args):
        if self.level >= args[-1]:
            self.add_exp(args[1])
            self.achievements.append(args[0])
            return self.achievements[-1]
        else:
            return "Not strong enough"
