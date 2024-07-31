from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def make_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.speed("fastest")
            x = 300
            y = randint(-250, 250)
            car.goto(x, y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def is_collided(self, turtle):
        for car in self.cars:
            if turtle.distance(car) <= 25:
                return True
        return False

