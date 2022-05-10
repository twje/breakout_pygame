import pygame


class ShapeRenderer:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.canvas = None
        self.position = None
        self.ppu = None
        self.color = (0, 0, 0)

    def set_color(self, color):
        self.color = color

    def line(self, x_start, y_start, x_end, y_end):
        x_start = self._transform_x(x_start)
        y_start = self._transform_y(y_start)
        x_end = self._transform_x(x_end)
        y_end = self._transform_y(y_end)
        pygame.draw.line(
            self.canvas,
            self.color,
            (x_start, y_start),
            (x_end, y_end)
        )

    def rect(self, x, y, width, height):
        x = self._transform_x(x)
        y = self._transform_y(y)
        width *= self.ppu.x
        height *= self.ppu.y
        pygame.draw.rect(
            self.canvas,
            self.color,
            (x, y, width, height),
            1,
        )

    def circle(self, x, y, radius):
        x = self._transform_x(x)
        y = self._transform_y(y)
        radius *= min(self.ppu.x, self.ppu.y)
        pygame.draw.circle(
            self.canvas,
            self.color,
            (x, y),
            radius,
            1
        )

    def sync(self, position, ppu):
        self.position = position
        self.ppu = ppu

    def begin(self):
        self.canvas = self.display_surface.copy()
        self.canvas = self.canvas.convert_alpha()
        self.canvas.fill((0, 0, 0, 0))

    def end(self):
        self.display_surface.blit(self.canvas, (0, 0))

    def dispose(self):
        pass

    def _transform_x(self, value):
        return self.position.x * self.ppu.x + value * self.ppu.x

    def _transform_y(self, value):
        return self.position.y * self.ppu.y + value * self.ppu.y
