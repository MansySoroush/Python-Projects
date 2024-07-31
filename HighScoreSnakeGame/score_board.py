from turtle import Turtle
from data import SCREEN_HEIGHT, SCREEN_TOP_MARGIN

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.init_high_score()
        self.init_board()

    def init_high_score(self):
        with open(file="./Files/score_file.txt", mode="r") as f:
            self.high_score = int(f.read())

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
        _text = f"Score: {self.score}, High Score: {self.high_score}"
        self.clear()
        self.write(_text, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def reset_me(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file="./Files/score_file.txt", mode="w") as f:
                f.write(f"{self.high_score}")

        self.score = 0
        self.update_board()

