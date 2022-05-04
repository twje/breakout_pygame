from core import Screen
from game_controller import GameController
from game_renderer import GameRenderer


class GameScreen(Screen):
    def __init__(self, game) -> None:
        super().__init__()
        self.game = game
        self.asset_manager = self.game.asset_manager
        self.batch = self.game.batch
        self.score_controller = self.game.score_controller

        self.controller = None
        self.renderer = None

    def show(self):
        self.controller = GameController(self.score_controller)
        self.renderer = GameRenderer(self.controller, self.batch, self.asset_manager)

    def handle_event(self, event):
        self.controller.handle_event(event)

    def render(self, delta):
        self.controller.update(delta)
        self.renderer.render(delta)

    def resize(self, width, height):
        self.renderer.resize(width, height)

    def hide(self):
        self.displose()

    def displose(self):
        self.renderer.dispose()
