from pygame.locals import *


class Game:
    def __init__(self):
        self.screen = None

    def set_screen(self, screen):
        self.screen = screen
        self.screen.show()
        self.screen.resize(self.window.width, self.window.height)

    def handle_event(self, event):
        if event.type == VIDEORESIZE:
            self.resize(event.w, event.h)
        else:
            self.screen.handle_event(event)

    def resize(self, width, height):
        self.screen.resize(width, height)

    def render(self, delta):
        self.screen.render(delta)

    def dispose(self):
        pass
