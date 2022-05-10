from copy import copy
from core import Camera
from core import ShapeRenderer
from core import FitViewPort
from utils import DebugCameraController
from utils import viewport_utils
from utils import ShapeRendererUtils
import game_config

from pygame import Vector2


class GameRenderer:
    def __init__(self, controller, batch, asset_manager):
        self.controller = controller
        self.batch = batch
        self.asset_manager = asset_manager

        self.camera = Camera()
        self.viewport = FitViewPort(
            game_config.WORLD_WIDTH,
            game_config.WORLD_HEIGHT,
            self.camera
        )
        self.renderer = ShapeRenderer()

        self.debugCameraController = DebugCameraController()
        self.debugCameraController.start_positon = Vector2(
            game_config.WORLD_CENTER_X,
            game_config.WORLD_CENTER_Y
        )

    def render(self, delta):
        self.debugCameraController.handleDebugInput(delta)
        self.debugCameraController.applyTo(self.camera)

        # clear screen
        self.render_debug()

    def resize(self, width, height):
        self.viewport.update(width, height)
        viewport_utils.debug_pixel_per_unit(self.viewport)

    def dispose(self):
        self.renderer.dispose()

    # Private Methods
    def render_debug(self):
        self.viewport.apply()  # apply ppu to camera

        if self.controller.draw_grid:
            viewport_utils.draw_grid(self.viewport, self.renderer)

        # draw debug
        self.renderer.sync(*self.camera.combined())
        self.renderer.begin()

        self.draw_debug()

        self.renderer.end()

    def draw_debug(self):
        old_color = copy(self.renderer.color)
        self.renderer.set_color((255, 0, 0))

        # paddle
        paddle_bounds = self.controller.paddle.bounds
        ShapeRendererUtils.rect(self.renderer, paddle_bounds)

        # bricks
        for brick in self.controller.bricks:
            ShapeRendererUtils.rect(self.renderer, brick.bounds)

        # circle
        ball_bounds = self.controller.ball.bounds
        ShapeRendererUtils.circle(self.renderer, ball_bounds)

        self.renderer.set_color(old_color)
