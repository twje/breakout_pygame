import pygame


class Window:
    def __init__(self, caption, width, height, event_callback):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(
            (width, height),
            pygame.RESIZABLE,
            32
        )
        self.event_callback = event_callback
        self.is_done = False
        self.is_focused = True
        self.is_maximized = True
        self.has_drawing_surface_state_changed = False

    @property
    def width(self):
        return self.screen.get_width()

    @property
    def height(self):
        return self.screen.get_height()

    def destroy(self):
        pygame.quit()

    def update(self):
        self.has_drawing_surface_state_changed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_done = True
            elif event.type == pygame.WINDOWFOCUSLOST:
                self.is_focused = False
                self.has_drawing_surface_state_changed = True
            elif event.type == pygame.WINDOWFOCUSGAINED:
                self.is_focused = True
                self.has_drawing_surface_state_changed = True
            elif event.type == pygame.WINDOWMAXIMIZED:
                self.is_maximized == True
                self.has_drawing_surface_state_changed = True
            elif event.type == pygame.WINDOWMINIMIZED:
                self.is_maximized = False
                self.has_drawing_surface_state_changed = True
            else:
                self.event_callback(event)

    def begin_render(self):
        self.screen.fill((68, 85, 90))

    def end_render(self):
        pygame.display.flip()
