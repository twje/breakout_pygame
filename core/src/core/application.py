from .window import Window
import pygame


class Application:
    def __init__(self, listener, caption, width, height):
        self.window = Window(caption, width, height, self.handle_event)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.elapsed_time = 0
        self.listener = listener

    def run(self):
        self.listener.create()
        
        while not self.window.is_done:
            self.update()
            self.render()
            self.restart_clock()
            
            #print(x)

        self.destroy()

    def handle_event(self, event):
        print(event)

        #self.listener.handle_event(event)        

    def update(self):
        self.window.update()
        if self.window.has_drawing_surface_state_changed:
            if not self.window.is_maximized:
                self.listener.
            else:
                self.listener.
        else:
            pass


    def render(self):
        self.window.begin_render()
        self.listener.render(self.elapsed_time)
        self.window.end_render()

    def restart_clock(self):
        self.elapsed_time = self.clock.tick(self.fps)/1000

    def destroy(self):
        self.window.destroy()
