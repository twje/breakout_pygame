from .window import Window
import pygame


class Application:
    def __init__(self, listener, caption, width, height):
        self.window = Window(self, caption, width, height)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.elapsed_time = 0
        self.listener = listener

    def run(self):
        self.create()
        while not self.window.is_done:
            self.window.update()
            self.render()
        self.destroy()

    def render(self):
        self.window.begin_render()
        self.listener.render(self.elapsed_time)
        self.window.end_render()

    def restart_clock(self):
        self.elapsed_time = self.clock.tick(self.fps)/1000

    def create(self):
        self.listener.create()
        self.listener.resize(self.window.width, self.window.height)

    def destroy(self):
        self.listener.pause()
        self.listener.dispose()
        self.window.destroy()

    # ----------------
    # Callback Methods
    # ----------------
    def handle_event(self, event):
        self.listener.handle_event(event)

    def minimized(self):
        self.listener.resize(0, 0)
        self.listener.pause()

    def maximized(self):
        self.resized()

    def restored(self, was_minimized):
        self.resized()
        if was_minimized:
            self.listener.resume()

    def resized(self):
        self.listener.resize(self.window.width, self.window.height)
