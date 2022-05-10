from utils.loading_screen_base import LoadingScreenBase


from utils import LoadingScreenBase
from game_screen import GameScreen
import game_config


class LoadingScreen(LoadingScreenBase):
    def __init__(self, game):
        super().__init__(game)

    def get_hud_width(self):
        return game_config.HUD_WIDTH

    def get_hud_height(self):
        return game_config.HUD_HEIGHT

    def on_load_done(self):
        self.game.set_screen(GameScreen(self.game))
