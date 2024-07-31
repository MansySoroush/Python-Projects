from turtle import Turtle
from data import PaddleSide, LEFT_PADDLE_START_POSITION, RIGHT_PADDLE_START_POSITION, PADDLE_DEF_SIZE

STEP_MOVEMENT = 20
PADDLE_WIDTH = PADDLE_DEF_SIZE * 5
PADDLE_HEIGHT = PADDLE_DEF_SIZE


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(PADDLE_WIDTH / PADDLE_DEF_SIZE, PADDLE_HEIGHT / PADDLE_DEF_SIZE)
        self.color("white")
        self.speed("fastest")
        self.side = side
        if side == PaddleSide["Left"]:
            self.goto(LEFT_PADDLE_START_POSITION)
        else:
            self.goto(RIGHT_PADDLE_START_POSITION)

    def reset_me(self):
        self.penup()
        if self.side == PaddleSide["Left"]:
            self.goto(LEFT_PADDLE_START_POSITION)
        else:
            self.goto(RIGHT_PADDLE_START_POSITION)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + STEP_MOVEMENT
        self.goto(x, y)

    def move_down(self):
        x = self.xcor()
        y = self.ycor() - STEP_MOVEMENT
        self.goto(x, y)
