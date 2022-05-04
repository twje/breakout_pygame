from tkinter import UNITS
from tkinter.tix import COLUMN


CAPTION = "Brick Breaker"

WIDTH = 1024     # pixels
HEIGHT = 768    # pixels

WORLD_WIDTH = 32    # world units
WORLD_HEIGHT = 24   # world units

WORLD_CENTER_X = WORLD_WIDTH/2  # world units
WORLD_CENTER_Y = WORLD_HEIGHT/2 # world units

PADDLE_WIDTH = 3    # world units
PADDLE_HEIGHT = 1   # world units
PADDLE_START_X = (WORLD_WIDTH - PADDLE_WIDTH)/2 # world units
PADDLE_START_Y = WORLD_HEIGHT - 2               # world units
PADDLE_VELOCITY_X = 15;  # world units

BRICK_WIDTH = 2.125  # world units
BRICK_HEIGHT = 1     # world units

LEFT_PAD = 0.5  # world units
TOP_PAD = 1.5   # world units

COLUMN_SPACING = 0.5 # world units
COLUMN_COUNT = 12

ROW_SPACING = 0.5 # world units
ROW_COUNT = 6

BALL_SIZE = .8                  # world units
BALL_HALF_SIZE = BALL_SIZE/2    # world units
BALL_START_X = PADDLE_START_X + PADDLE_WIDTH/2
BALL_START_Y = PADDLE_START_Y - BALL_HALF_SIZE
BALL_VELOCITY = 14
BALL_START_ANGLE = 60

BRICK_SCORE = 10