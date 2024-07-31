from turtle import Turtle
from data import SCREEN_HEIGHT, PaddleSide, SCREEN_TOP_MARGIN

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()

    def update_board(self):
        self.clear()

        left_x_pos = -70
        right_x_pos = 70
        y_pos = int(SCREEN_HEIGHT / 2) - SCREEN_TOP_MARGIN

        self.goto(x=left_x_pos, y=y_pos)
        self.write(f"{self.left_score}", align=ALIGNMENT, font=FONT)
        self.goto(x=right_x_pos, y=y_pos)
        self.write(f"{self.right_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, winner_side):
        if winner_side == PaddleSide["Left"]:
            self.left_score += 1
        else:
            self.right_score += 1

        self.update_board()

    def reset_scores(self):
        self.left_score = 0
        self.right_score = 0
        self.update_board()
