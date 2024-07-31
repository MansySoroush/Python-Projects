from turtle import Turtle
from random import randint
from data import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, SCREEN_TOP_MARGIN


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.make_food()

    def make_food(self):
        self.penup()
        permitted_width = SCREEN_WIDTH - 2 * SNAKE_SIZE
        permitted_height = SCREEN_HEIGHT - 2 * SNAKE_SIZE - SCREEN_TOP_MARGIN
        x = randint((-1)*int((permitted_width / 2)), int(permitted_width / 2))
        y = randint((-1)*int((permitted_height / 2)), int(permitted_height / 2))
        self.goto(x, y)

    def reposition(self):
        self.make_food()
