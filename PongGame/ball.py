from turtle import Turtle
from data import BallDirection, BALL_DIAMETER

DEF_DIAMETER = 20
START_POSITION = (0, 0)
STEP_MOVEMENT = BALL_DIAMETER / 2
INIT_MOVE_SPEED = 0.1
FACTOR_MOVE_SPEED = 0.9

class Ball(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.move_direction = direction
        self.shape("circle")
        self.penup()
        self.shapesize(BALL_DIAMETER / DEF_DIAMETER, BALL_DIAMETER / DEF_DIAMETER)
        self.color("white")
        self.speed("fastest")
        self.goto(START_POSITION)
        self.move_speed = INIT_MOVE_SPEED

    def reset_me(self):
        if self.move_direction == BallDirection["UpLeft"]:
            self.move_direction = BallDirection["UpRight"]
        elif self.move_direction == BallDirection["UpRight"]:
            self.move_direction = BallDirection["UpLeft"]
        elif self.move_direction == BallDirection["DownRight"]:
            self.move_direction = BallDirection["DownLeft"]
        elif self.move_direction == BallDirection["DownLeft"]:
            self.move_direction = BallDirection["DownRight"]

        self.move_speed = INIT_MOVE_SPEED
        self.penup()
        self.goto(START_POSITION)

    def move(self):
        x_step = STEP_MOVEMENT
        y_step = STEP_MOVEMENT

        if self.move_direction == BallDirection["UpLeft"] or self.move_direction == BallDirection["DownLeft"]:
            x_step *= (-1)

        if self.move_direction == BallDirection["DownRight"] or self.move_direction == BallDirection["DownLeft"]:
            y_step *= (-1)

        x = self.xcor() + x_step
        y = self.ycor() + y_step
        self.goto(x, y)

    def bounce_top(self):
        if self.move_direction == BallDirection["UpRight"]:
            self.move_direction = BallDirection["DownRight"]
        elif self.move_direction == BallDirection["UpLeft"]:
            self.move_direction = BallDirection["DownLeft"]

    def bounce_bottom(self):
        if self.move_direction == BallDirection["DownRight"]:
            self.move_direction = BallDirection["UpRight"]
        elif self.move_direction == BallDirection["DownLeft"]:
            self.move_direction = BallDirection["UpLeft"]

    def bounce_right(self):
        if self.move_direction == BallDirection["DownRight"]:
            self.move_direction = BallDirection["DownLeft"]
        elif self.move_direction == BallDirection["UpRight"]:
            self.move_direction = BallDirection["UpLeft"]
        self.move_speed *= FACTOR_MOVE_SPEED

    def bounce_left(self):
        if self.move_direction == BallDirection["DownLeft"]:
            self.move_direction = BallDirection["DownRight"]
        elif self.move_direction == BallDirection["UpLeft"]:
            self.move_direction = BallDirection["UpRight"]
        self.move_speed *= FACTOR_MOVE_SPEED
