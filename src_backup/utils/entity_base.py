

class EntityBase:
    def __init__(self):
        self.x = 0
        self.y = 0

    # --------------
    # Public Methods
    # --------------
    def set_position(self, x, y):
        self.x = x
        self.y = y
