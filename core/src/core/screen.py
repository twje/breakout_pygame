class Screen:
    def dispose(self):
        """Called when this screen should release all resources."""
        pass

    def hide(self):
        """Called when this screen is no longer the current screen for a Game."""
        pass

    def pause(self):
        pass

    def render(self, delta):
        """Called when the screen should render itself."""
        pass

    def resize(self, width, height):
        pass

    def resume(self):
        pass

    def show(self):
        """Called when this screen becomes the current screen for a Game."""

    def handle_event(self, event):
        pass
