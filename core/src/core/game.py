"""
Screens are not disposed automatically. You must handle whether you want to keep screens around or dispose of them when another
screen is set.
"""
import pygame
from .application_listener import ApplicationListener


class Game(ApplicationListener):
    def __init__(self) -> None:
        super().__init__()
        self._screen = None

    @property
    def screen(self):
        return self._screen

    @screen.getter
    def screen(self, value):
        if self.screen is not None:
            self.screen.hide()

        self.screen = value
        if self.screen is not None:
            surface = pygame.display.get_surface()
            self.screen.show()
            self.screen.resize(surface.get_width(), surface.get_height())

    def dispose(self):
        if self.screen is not None:
            self.screen.hide()

    def pause(self):
        if self.screen is not None:
            self.screen.pause()

    def render(self, delta):
        if self.screen is not None:
            self.screen.render(delta)

    def resize(self, width, height):
        if self.screen is not None:
            self.screen.resize(width, height)

    def resume(self):
        if self.screen is not None:
            self.screen.resume()

    def handle_event(self, event):
        if self.screen is not None:
            self.screen.handle_event(event)
