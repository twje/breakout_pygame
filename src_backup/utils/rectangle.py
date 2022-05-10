from dataclasses import dataclass
from pygame import Vector2

@dataclass
class Rectangle:
    x: float = 0
    y: float = 0
    width: float = 0
    height: float = 0

    @property
    def top_left(self):
        return Vector2(self.x, self.y)
    
    @property
    def top_right(self):
        return Vector2(self.x + self.width, self.y)

    @property
    def bottom_left(self):
        return Vector2(self.x, self.y + self.height)
    
    @property
    def bottom_right(self):
        return Vector2(self.x + self.width, self.y + self.height)
