from turtle import Turtle
from data import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, SCREEN_TOP_MARGIN

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.init_board()

    def init_board(self):
        self.penup()
        self.speed("fastest")
        self.color("white")

        x_pos = 0
        y_pos = int(SCREEN_HEIGHT / 2) - SCREEN_TOP_MARGIN

        self.hideturtle()
        self.goto(x=x_pos, y=y_pos)
        self.update_board()

    def update_board(self):
        _text = f"Score: {self.score}"
        self.clear()
        self.write(_text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
