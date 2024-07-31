from turtle import Screen
from data import (SCREEN_WIDTH, SCREEN_HEIGHT, BallDirection, PaddleSide, BALL_DIAMETER,
                  MIN_DISTANCE_BETWEEN_BALL_AND_PADDLE, PADDLE_DEF_SIZE)
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")

# Turn off the screen
screen.tracer(0)

left_paddle = Paddle(PaddleSide["Left"])
right_paddle = Paddle(PaddleSide["Right"])
_ball = Ball(BallDirection["UpRight"])
score_board = ScoreBoard()

game_is_on = True


def reset_game():
    _ball.reset_me()
    # left_paddle.reset_me()
    # right_paddle.reset_me()


def terminate_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="a", fun=terminate_game)

while game_is_on:
    # To refresh after each movement
    screen.update()
    time.sleep(_ball.move_speed)

    # To detect collision with top and bottom walls
    top_wall = int(SCREEN_HEIGHT / 2 - BALL_DIAMETER)
    bottom_wall = (-1) * int(SCREEN_HEIGHT / 2 - BALL_DIAMETER)

    if _ball.ycor() > top_wall:
        _ball.bounce_top()
    elif _ball.ycor() < bottom_wall:
        _ball.bounce_bottom()

    # To detect collision with paddles
    if (_ball.distance(right_paddle) < MIN_DISTANCE_BETWEEN_BALL_AND_PADDLE and
            _ball.xcor() + BALL_DIAMETER > right_paddle.xcor()):
        _ball.bounce_right()
    elif (_ball.distance(left_paddle) < MIN_DISTANCE_BETWEEN_BALL_AND_PADDLE and
          _ball.xcor() < left_paddle.xcor() + PADDLE_DEF_SIZE):
        _ball.bounce_left()
    elif _ball.xcor() + BALL_DIAMETER > SCREEN_WIDTH / 2:
        reset_game()
        score_board.increase_score(PaddleSide["Left"])
    elif _ball.xcor() < (-1) * (SCREEN_WIDTH / 2):
        reset_game()
        score_board.increase_score(PaddleSide["Right"])

    _ball.move()

screen.exitonclick()
