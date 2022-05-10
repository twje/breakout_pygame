from utils import EntityBase
from utils import Rectangle


class Brick(EntityBase):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def set_size(self, width, height):
        self.width = width
        self.height = height

    @property
    def bounds(self):
        return Rectangle(self.x, self.y, self.width, self.height)
