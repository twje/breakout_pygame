import pygame
import game_config


class PaddleInputController:
    def __init__(self, paddle):
        self.paddle = paddle

    def update(self, delta):
        velocity_x = 0        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:            
            velocity_x = -game_config.PADDLE_VELOCITY_X
        if keys[pygame.K_RIGHT]:
            
            velocity_x = game_config.PADDLE_VELOCITY_X

        self.paddle.velocity.x = velocity_x        
