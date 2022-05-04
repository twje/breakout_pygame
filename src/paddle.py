from utils import EntityBase
from pygame import Vector2
from utils import Rectangle


class Paddle(EntityBase):
    def __init__(self):
        super().__init__()
        self.velocity = Vector2()
        self.width = 0
        self.height = 0

    def set_size(self, width, height):
        self.width = width
        self.height = height

    @property
    def bounds(self):
        return Rectangle(self.x, self.y, self.width, self.height)

    def update(self, delta):        
        self.x += self.velocity.x * delta
