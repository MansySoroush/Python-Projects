from turtle import Screen
from snake import Snake
import time
from data import SCREEN_WIDTH, SCREEN_HEIGHT
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")

# Turn off the screen
screen.tracer(0)

_score_board = ScoreBoard()
_snake = Snake()
_food = Food()

screen.listen()
screen.onkey(key="Up", fun=_snake.move_up)
screen.onkey(key="Down", fun=_snake.move_down)
screen.onkey(key="Left", fun=_snake.move_left)
screen.onkey(key="Right", fun=_snake.move_right)

game_is_on = True

while game_is_on:
    # To refresh after each movement
    screen.update()
    time.sleep(0.1)
    _snake.move()

    # To detect collision
    if _snake.head.distance(_food) < 15:
        _food.reposition()
        _score_board.increase_score()
        _snake.extend()

    # To detect collision with wall
    right_wall = int(SCREEN_WIDTH / 2)
    left_wall = (-1) * int(SCREEN_WIDTH / 2)
    top_wall = int(SCREEN_HEIGHT / 2)
    bottom_wall = (-1) * int(SCREEN_HEIGHT / 2)
    x = _snake.head.xcor()
    y = _snake.head.ycor()
    game_is_on = not _snake.is_self_collision() and (left_wall < x < right_wall) and (bottom_wall < y < top_wall)

    if not game_is_on:
        _score_board.game_over()

screen.exitonclick()
