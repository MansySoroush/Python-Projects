SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_LEFT_MARGIN = 50
SCREEN_RIGHT_MARGIN = 50
SCREEN_TOP_MARGIN = 30

BALL_DIAMETER = 20
PADDLE_DEF_SIZE = 20
MIN_DISTANCE_BETWEEN_BALL_AND_PADDLE = BALL_DIAMETER + PADDLE_DEF_SIZE + 10

PaddleSide = {
    "Right": 0,
    "Left": 1
}

BallDirection = {
    "UpRight": 0,
    "DownRight": 1,
    "UpLeft": 2,
    "DownLeft": 3
}

RIGHT_PADDLE_START_POSITION = (int(SCREEN_WIDTH / 2) - SCREEN_RIGHT_MARGIN, 0)
LEFT_PADDLE_START_POSITION = ((-1) * int(SCREEN_WIDTH / 2) + SCREEN_LEFT_MARGIN, 0)
