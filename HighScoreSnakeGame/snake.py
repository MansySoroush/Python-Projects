from turtle import Turtle
from data import direction, SNAKE_SIZE


class Snake:
    def __init__(self):
        self.segments = []
        self.make_snake()
        self.head = self.segments[0]

    def make_snake(self):
        x_pos = 0
        y_pos = 0

        for i in range(0, 3):
            pos = (x_pos, y_pos)
            self.make_segment(pos)
            x_pos -= SNAKE_SIZE

    def make_segment(self, pos):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(pos)
        self.segments.append(seg)

    def extend(self):
        last_segment = self.segments[-1]
        self.make_segment(last_segment.position())

    def is_self_collision___(self):
        for seg in self.segments:
            if seg == self.head:
                pass
            elif self.head.distance(seg) < int(SNAKE_SIZE / 2):
                return True
        return False

    def is_self_collision(self):
        for seg in self.segments[1:]:
            if self.head.distance(seg) < int(SNAKE_SIZE / 2):
                return True
        return False

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)

        self.head.forward(SNAKE_SIZE)

    def move_up(self):
        if self.head.heading() != direction["Down"]:
            self.head.setheading(direction["Up"])

    def move_down(self):
        if self.head.heading() != direction["Up"]:
            self.head.setheading(direction["Down"])

    def move_left(self):
        if self.head.heading() != direction["Right"]:
            self.head.setheading(direction["Left"])

    def move_right(self):
        if self.head.heading() != direction["Left"]:
            self.head.setheading(direction["Right"])

    def reset_me(self):
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()

        self.make_snake()
        self.head = self.segments[0]

