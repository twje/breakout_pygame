from preference import Preference


class ScoreController:
    HIGH_SCORE_KEY = "highScore"

    def __init__(self):
        self.prefs = Preference("preference")
        self.high_score = self.prefs.get_preference(self.HIGH_SCORE_KEY, 0)
        self.score = 0

    def reset(self):
        self.score = 0

    def add_score(self, value):
        self.score += value

    def update_high_score(self):
        if self.score < self.high_score:
            return

        self.high_score = self.score
        self.prefs.add_preference(self.HIGH_SCORE_KEY, self.high_score)
        self.prefs.flush()
