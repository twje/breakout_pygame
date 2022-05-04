from core import Screen
from core import Camera
from core import FitViewPort
from core import ShapeRenderer


class LoadingScreenBase(Screen):
    DEFAULT_HUD_WIDTH = 640
    DEFAULT_HUD_HEIGHT = 480
    DEFAULT_PROGRESS_BAR_HEIGHT = 60

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.asset_manager = self.game.asset_manager
        self.camera = None
        self.viewport = None
        self.renderer = None

        self.progress = 0
        self.wait_time = 0.75

        self.hud_width = None
        self.hud_height = None

        self.progress_bar_width = None
        self.progress_bar_height = None

        self.change_screen = False

    # -----------------
    # Lifecycle Methods
    # -----------------
    def show(self):
        self.hud_width = self.get_hud_width()
        self.hud_height = self.get_hud_height()

        self.progress_bar_width = self.get_progress_bar_width()
        self.progress_bar_height = self.get_progress_bar_height()

        self.camera = Camera()
        self.viewport = FitViewPort(
            self.hud_width,
            self.hud_height,
            self.camera
        )
        self.renderer = ShapeRenderer()

        # Asset descriptors (think about)

    def resize(self, width, height):
        self.viewport.update(width, height)

    def dispose(self):
        self.renderer.dispose()

    def render(self, delta):
        self._update(delta)

        self.viewport.apply()
        self.renderer.sync(*self.camera.combined())
        self.renderer.begin()

        self._draw()

        self.renderer.end()

        if (self.change_screen):
            self.on_load_done()

    # -----
    # Hooks
    # -----
    def get_hud_width(self):
        pass

    def get_hud_height(self):
        pass

    def get_progress_bar_width():
        pass

    def get_progress_bar_height():
        pass

    def on_load_done(self):
        pass

    # ---------------
    # Private Methods
    # ---------------
    def _update(self, delta):
        self.progress = self.asset_manager.get_progress()

        if self.asset_manager.update():
            self.wait_time -= delta

            if self.wait_time <= 0:
                self.change_screen = True

    def _draw(self):
        pass
