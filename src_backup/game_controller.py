from traceback import print_tb
from turtle import back

import pygame
from entity_factory import EntityFactory
from paddle_input_controller import PaddleInputController
from utils import intersector
import game_config


class GameController:
    def __init__(self, score_controller):
        self.score_controller = score_controller
        self.factory = EntityFactory()
        self.paddle = self.factory.create_paddle()
        self.paddle_input_controller = PaddleInputController(self.paddle)
        self.bricks = []
        self.ball = self.factory.create_ball()
        self.is_just_touched = False
        self.draw_grid = False

        self.start_level()

    def start_level(self):
        self.bricks = self.factory.create_bricks()
        self.paddle.set_position(
            game_config.PADDLE_START_X, game_config.PADDLE_START_Y)
        self.ball.set_position(game_config.BALL_START_X,
                               game_config.BALL_START_Y)
        self.ball.stop()
        self.is_just_touched = False

    def activate_ball(self):
        self.ball.set_velocity(
            game_config.BALL_START_ANGLE, game_config.BALL_VELOCITY)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F5:
                self.toggle_debug_grid()
            else:
                self.is_just_touched = True

    def toggle_debug_grid(self):
        self.draw_grid = not self.draw_grid

    def update(self, delta):
        if self.ball.is_not_active() and self.is_just_touched:
            self.activate_ball()

        if self.ball.is_not_active():
            return

        # update paddle
        self.paddle_input_controller.update(delta)
        self.paddle.update(delta)

        # block paddle from leaveing world
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle.width >= game_config.WORLD_WIDTH:
            self.paddle.x = game_config.WORLD_WIDTH - self.paddle.width

        self.ball.update(delta)

        # block ball from leaving world
        if self.ball.y - game_config.BALL_HALF_SIZE <= 0:
            self.ball.y = game_config.BALL_HALF_SIZE
            self.ball.multiply_velocity_y(-1)

        max_y = self.ball.y + self.ball.radius
        if max_y >= game_config.WORLD_HEIGHT:
            self.ball.y = game_config.WORLD_HEIGHT - self.ball.radius
            self.ball.multiply_velocity_y(-1)

        if self.ball.x - game_config.BALL_HALF_SIZE <= 0:
            self.ball.x = game_config.BALL_HALF_SIZE
            self.ball.multiply_velocity_x(-1)

        if self.ball.x + self.ball.radius >= game_config.WORLD_WIDTH:
            self.ball.x = game_config.WORLD_WIDTH - self.ball.radius
            self.ball.multiply_velocity_x(-1)

        self.check_collission()

        # victory condition
        if len(self.bricks) == 0:
            self.start_level()

    def check_collission(self):
        self.check_ball_with_paddle_collission()
        self.check_ball_with_brick_collision()

    def check_ball_with_paddle_collission(self):
        ball_bounds = self.ball.bounds
        paddle_bounds = self.paddle.bounds
        if intersector.circle_rectangle_collide(ball_bounds, paddle_bounds):
            ball_center_x = ball_bounds.x + ball_bounds.radius/2
            percent = (ball_center_x - paddle_bounds.x) / \
                paddle_bounds.width  # 0-1

            # interpolate angle between 150 and 30
            bounce_angle = 150 - percent * 120
            self.ball.set_velocity(bounce_angle, self.ball.speed)

    def check_ball_with_brick_collision(self):
        ball_bounds = self.ball.bounds
        for brick in list(self.bricks):
            brick_bounds = brick.bounds
            if not intersector.circle_rectangle_collide(ball_bounds, brick_bounds):
                continue

            top_hit = intersector.circle_segment_collide(
                ball_bounds, brick_bounds.top_left, brick_bounds.top_right)
            bottom_hit = intersector.circle_segment_collide(
                ball_bounds, brick_bounds.bottom_left, brick_bounds.bottom_right)
            left_hit = intersector.circle_segment_collide(
                ball_bounds, brick_bounds.top_left, brick_bounds.bottom_left)
            right_hit = intersector.circle_segment_collide(
                ball_bounds, brick_bounds.top_right, brick_bounds.bottom_right)

            if top_hit and self.ball.velocity.y < 0:
                self.ball.multiply_velocity_y(-1)
            elif bottom_hit and self.ball.velocity.y > 0:
                self.ball.multiply_velocity_y(-1)

            if left_hit and self.ball.velocity.x > 0:
                self.ball.multiply_velocity_x(-1)
            elif right_hit and self.ball.velocity.x < 0:
                self.ball.multiply_velocity_x(-1)

            self.bricks.remove(brick)
            self.score_controller.add_score(game_config.BRICK_SCORE)
            print(f"current score = {self.score_controller.score}")
