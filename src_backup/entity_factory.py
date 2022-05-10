from paddle import Paddle
from brick import Brick
from ball import Ball
import game_config


class EntityFactory:
    def create_ball(self):
        ball = Ball()
        ball.set_position(game_config.BALL_START_X, game_config.BALL_START_Y)
        ball.radius = game_config.BALL_HALF_SIZE
        ball.set_velocity(game_config.BALL_START_ANGLE, game_config.BALL_VELOCITY)
        return ball

    def create_paddle(self):
        paddle = Paddle()
        paddle.set_position(
            game_config.PADDLE_START_X,
            game_config.PADDLE_START_Y
        )
        paddle.set_size(game_config.PADDLE_WIDTH, game_config.PADDLE_HEIGHT)
        return paddle

    def create_bricks(self):
        bricks = []
        start_x = game_config.LEFT_PAD
        start_y = game_config.TOP_PAD

        for row in range(game_config.ROW_COUNT):
            brick_y = start_y + row * \
                (game_config.ROW_SPACING + game_config.BRICK_HEIGHT)

            for col in range(game_config.COLUMN_COUNT):
                brick_x = start_x + col * \
                    (game_config.BRICK_WIDTH + game_config.COLUMN_SPACING)

                bricks.append(self._create_brick(brick_x, brick_y))
        return bricks

    def _create_brick(self, x, y):
        brick = Brick()
        brick.set_position(x, y)
        brick.set_size(game_config.BRICK_WIDTH, game_config.BRICK_HEIGHT)
        return brick
