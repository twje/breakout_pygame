from pygame import Vector2


class DebugCameraController:
    def __init__(self):
        self.start_positon = Vector2()

    def handleDebugInput(self, delta):
        pass

    def applyTo(self, camera):
        camera.position = Vector2(self.start_positon.x, self.start_positon.y)
