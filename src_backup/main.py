from core import Application
from brick_breaker_game import BrickBreakerGame
import game_config


def main():
    app = Application(
        BrickBreakerGame,
        game_config.CAPTION,
        game_config.WIDTH,
        game_config.HEIGHT
    )

    app.run()


if __name__ == "__main__":
    main()
