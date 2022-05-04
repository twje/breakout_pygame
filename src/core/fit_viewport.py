from pygame import Vector2


class FitViewPort:
    def __init__(self, world_width, world_height, camera):
        self.world_width = world_width
        self.world_height = world_height
        self.screen_width = None
        self.screen_height = None
        self.camera = camera

    def update(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self):
        x_ppu = self.screen_width/self.world_width
        y_ppu = self.screen_height/self.world_height
        self.camera.ppu = Vector2(x_ppu, y_ppu)
        self.camera.world_width = self.world_width
        self.camera.world_height = self.world_height
