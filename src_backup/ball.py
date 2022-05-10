
from pygame import Vector2

from utils import math_utils
from utils import EntityBase
from utils import Circle


class Ball(EntityBase):
    def __init__(self):
        super().__init__()
        self.velocity = Vector2()
        self.x = 0
        self.y = 0
        self.radius = 0

    @property
    def speed(self):
        return self.velocity.magnitude()

    @property
    def bounds(self):
        return Circle(self.x, self.y, self.radius)

    def update(self, delta):
        new_x = self.x + self.velocity.x * delta
        new_y = self.y - self.velocity.y * delta
        self.set_position(new_x, new_y)

    def set_velocity(self, angle_deg, value):        
        self.velocity.x = math_utils.cos_deg(angle_deg) * value
        self.velocity.y = math_utils.sin_deg(angle_deg) * value

    def multiply_velocity_x(self, value):
        self.velocity.x *= value

    def multiply_velocity_y(self, value):
        self.velocity.y *= value

    def stop(self):
        self.velocity.x = 0
        self.velocity.y = 0
    
    def is_not_active(self):
        return self.velocity.x == 0 and self.velocity.y == 0
