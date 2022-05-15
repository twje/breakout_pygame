from core import ApplicationListener


class Breakout(ApplicationListener):
    def __init__(self):
        super().__init__()

    def create(self):
        print("create")

    def dispose(self):
        print("dispose")

    def pause(self):
        print("pause")

    def render(self, delta):
        pass

    def resize(self, width, height):
        print("resize")

    def resume(self):
        print("resume")

    def handle_event(self, event):
        pass
