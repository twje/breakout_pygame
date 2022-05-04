from utils import GameBase
from game_screen import GameScreen
from score_controller import ScoreController


class BrickBreakerGame(GameBase):
    def __init__(self):
        super().__init__()
        self.score_controller = None

    def post_create(self):
        self.score_controller = ScoreController()
        self.set_screen(GameScreen(self))
