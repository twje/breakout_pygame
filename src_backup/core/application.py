from .window import Window
import pygame


class Application:
    def __init__(self, game, width, height, caption):        
        self.window = Window(width, height, caption, self.handle_event)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.elapsed_time = 0
        self.game = game()

    def run(self):        
        while not self.window.is_done:
            self.update()
            self.render()
            self.restart_clock()

        self.destroy()

    def handle_event(self, event):
        self.game.handle_event(event)

    def update(self):
        self.window.update()

    def render(self):
        self.window.begin_render()
        self.game.render(self.elapsed_time)
        self.window.end_render()

    def restart_clock(self):
        self.elapsed_time = self.clock.tick(self.fps)/1000

    def destroy(self):
        self.window.destroy()
