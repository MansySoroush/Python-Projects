from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()

        x_pos = -250
        y_pos = 250

        self.goto(x=x_pos, y=y_pos)
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over!", align="center", font=FONT)
