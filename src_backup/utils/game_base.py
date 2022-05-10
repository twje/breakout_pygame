from core import Game


class GameBase(Game):
    def __init__(self):
        super().__init__()
        self.asset_manager = None   # create
        self.batch = None           # create
        self.post_create()

    def post_create(self):
        pass

    def dispose(self):
        super().dispose()
        self.asset_manager.dispose()
        self.batch.dispose()
