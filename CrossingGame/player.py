from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.shapesize(1, 1, 1)
        self.setheading(90)
        self.init_player_pos()

    def init_player_pos(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.init_player_pos()

    def is_successful_crossed(self):
        return self.ycor() > 280


