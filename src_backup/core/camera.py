from pygame import Vector2


class Camera:
    def __init__(self):
        self.world_width = 0
        self.world_height = 0
        self.position = Vector2()
        self.ppu = Vector2()

    def combined(self):
        half_world = Vector2(self.world_width/2, -self.world_height/2)
        offset = half_world - Vector2(self.position.x, -self.position.y)
        print(self.position)
        return offset, self.ppu
