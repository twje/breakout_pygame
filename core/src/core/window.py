import pygame


class Window:
    def __init__(self, application, caption, width, height):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(
            (width, height),
            pygame.RESIZABLE,
            32
        )
        self.application = application
        self.is_done = False
        self.prv_event = None

    @property
    def width(self):
        return self.screen.get_width()

    @property
    def height(self):
        return self.screen.get_height()

    def was_window_minimized(self):
        if self.prv_event is None:
            return False
        return self.prv_event.type == pygame.WINDOWMINIMIZED

    def destroy(self):
        pygame.quit()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = True
            elif event.type == pygame.WINDOWMAXIMIZED:
                self.application.maximized()
                self.prv_event = event
            elif event.type == pygame.WINDOWMINIMIZED:
                self.application.minimized()
                self.prv_event = event
            elif event.type == pygame.WINDOWRESTORED:
                self.application.restored(self.was_window_minimized())
                self.prv_event = event
            elif event.type == pygame.WINDOWRESIZED:
                self.application.resized()
                self.prv_event = event

            self.application.handle_event(event)

    def begin_render(self):
        self.screen.fill((68, 85, 90))

    def end_render(self):
        pygame.display.flip()
