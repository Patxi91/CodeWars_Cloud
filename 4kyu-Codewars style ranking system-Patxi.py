
class User:

    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = self.ranks[0]
        self.progress = 0

    def inc_progress(self, activity_rank):
        if activity_rank in self.ranks:
            earned_progress = 0
            d = self.ranks.index(activity_rank)-self.ranks.index(self.rank)
            if self.progress < 100 and self.rank != self.ranks[-1]:
                if d > 0:
                    earned_progress = 10 * d * d
                    self.progress_score(earned_progress)
                elif d == 0:
                    earned_progress = 3
                    self.progress_score(earned_progress)
                elif d == -1:
                    earned_progress = 1
                    self.progress_score(earned_progress)
                elif d <= -2:  # Activities 2 or more levels lower
                    pass
            else:
                if self.rank != self.ranks[-1]:
                    self.rank = self.ranks[self.ranks.index(self.rank) + 1]  # next rank
                    self.progress -= 100
                    self.inc_progress(activity_rank)
                else:
                    self.progress = 0
        else:
            if self.rank == -7 or self.rank == -8:
                if self.progress < 100:
                    pass
                else:
                    while self.progress >= 100 and self.rank != self.ranks[-1]:
                        self.rank = self.ranks[self.ranks.index(self.rank) + 1]  # next rank
                        if self.rank != self.ranks[-1]:
                            self.progress -= 100
                        else:
                            self.progress = 0
            else:
                print(activity_rank)
                raise Exception("Wrong activity level.")

    def progress_score(self, earned_progress):
        if self.rank != self.ranks[-1]:
            self.progress += earned_progress
            self.inc_progress(self.ranks[self.ranks.index(self.rank) - 2] if self.rank > -7 else -10)  # This activity rank will give 0 earned progress

