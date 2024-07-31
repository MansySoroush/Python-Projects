from data import color_names, walk_direction, directions
from random import choice, randint
import turtle as turtle_module
# import colorgram

MIN_SIDE_POLYGON = 3
MAX_WALK_COUNT = 200
SPIRO_GRAPH_RADIUS = 70
DISTANCE_BETWEEN_SPOTS = 20


def choose_color() -> str:
    return choice(color_names)


def random_rgb_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def get_direction() -> str:
    return choice(walk_direction)


def get_angle() -> int:
    return choice(directions)


class PaintManager:
    def __init__(self, turtle):
        self.turtle = turtle
        self.extracted_colors = []

        turtle_module.colormode(255)

    def draw_square(self) -> None:
        self.turtle.penup()
        self.turtle.goto(-100, 200)
        self.turtle.pendown()

        self.turtle.shape("turtle")
        self.turtle.color(choose_color())

        for n in range(0, 4):
            self.turtle.forward(150)
            self.turtle.right(90)

    def draw_dashed_line(self, length, dash_length):
        self.turtle.penup()
        self.turtle.goto(-100, 200)
        self.turtle.pendown()
        self.turtle.shape("triangle")
        self.turtle.pensize(2)
        self.turtle.shapesize(0.5, 0.5, 1)
        self.turtle.color(choose_color())

        # Calculate the number of segments
        segments = int(length / dash_length)

        # Draw each segment
        for _ in range(segments):
            self.turtle.forward(dash_length)
            self.turtle.penup()  # Lift the pen
            self.turtle.forward(dash_length)
            self.turtle.pendown()  # Lower the pen

    def draw_polygon(self, s_cnt):
        for n in range(0, s_cnt):
            self.turtle.forward(100)
            self.turtle.right(360 / s_cnt)

    def set_random_rgb_pen_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        self.turtle.pencolor(r, g, b)

    def draw_complex_shape(self, max_sides):
        if max_sides <= MIN_SIDE_POLYGON:
            max_sides = MIN_SIDE_POLYGON

        start = MIN_SIDE_POLYGON
        end = max_sides

        self.turtle.penup()
        self.turtle.goto(-100, 200)
        self.turtle.pendown()
        self.turtle.shape("triangle")
        self.turtle.pensize(2)
        self.turtle.shapesize(0.5, 0.5, 1)

        for n in range(start, end + 1):
            self.turtle.color(choose_color())
            self.draw_polygon(s_cnt=n)

    def draw_random_walk(self):
        self.turtle.penup()
        self.turtle.goto(-100, 50)
        self.turtle.pendown()
        self.turtle.shape("circle")
        self.turtle.pensize(5)
        self.turtle.shapesize(0.3, 0.3, 1)
        self.turtle.speed("fastest")

        for _ in range(MAX_WALK_COUNT):
            # self.set_random_rgb_pen_color()
            self.turtle.pencolor(random_rgb_color())
            steps = randint(2, 10) * 3
            self.turtle.forward(steps)
            self.turtle.setheading(get_angle())

    def draw_random_walk___(self):
        self.turtle.penup()
        self.turtle.goto(-100, 50)
        self.turtle.pendown()
        self.turtle.shape("circle")
        self.turtle.pensize(5)
        self.turtle.shapesize(0.3, 0.3, 1)

        angle = 0

        for _ in range(MAX_WALK_COUNT):
            direction = get_direction()
            if direction == "right":
                angle = 90
            elif direction == "left":
                angle = 270
            elif direction == "back":
                angle = 180

            self.turtle.color(choose_color())
            self.turtle.right(angle)

            steps = randint(2, 10) * 3
            self.turtle.forward(steps)

    def draw_spiro_graph(self, size_of_gap):
        self.turtle.penup()
        self.turtle.goto(-50, 100)
        self.turtle.pendown()
        self.turtle.shape("circle")
        self.turtle.pensize(1)
        self.turtle.shapesize(0.1, 0.1, 1)
        self.turtle.speed("fastest")

        for n in range(0, 360, size_of_gap):
            self.turtle.setheading(n)
            self.turtle.pencolor(random_rgb_color())
            self.turtle.circle(SPIRO_GRAPH_RADIUS)

    def extract_colors_from_image(self, image_name, count):
        if len(self.extracted_colors) > 0:
            self.extracted_colors.clear()

        colors = colorgram.extract(image_name, count)
        for color in colors:
            self.extracted_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

    def draw_dot___(self, color):
        self.turtle.pencolor(color)
        self.turtle.forward(1)
        self.turtle.penup()  # Lift the pen
        self.turtle.forward(DISTANCE_BETWEEN_SPOTS)
        self.turtle.pendown()  # Lower the pen

    def draw_dot(self, color):
        self.turtle.dot(10, color)
        self.turtle.penup()  # Lift the pen
        self.turtle.forward(DISTANCE_BETWEEN_SPOTS)
        self.turtle.pendown()  # Lower the pen

    def draw_spots___(self, x_count, y_count):
        self.turtle.penup()
        self.turtle.goto(-100, -50)
        self.turtle.pendown()
        self.turtle.shape("circle")
        self.turtle.pensize(10)
        self.turtle.shapesize(0.1, 0.1, 1)
        self.turtle.speed("fastest")

        for x in range(x_count):
            for y in range(y_count):
                color = choice(self.extracted_colors) if len(self.extracted_colors) == 0 else random_rgb_color()
                self.draw_dot___(color)

            self.turtle.penup()
            curr_pos = self.turtle.pos()
            self.turtle.goto(-100, curr_pos[1] + DISTANCE_BETWEEN_SPOTS)
            self.turtle.pendown()

    def draw_spots(self, x_count, y_count):
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-100, -50)
        self.turtle.pendown()
        self.turtle.shape("circle")
        self.turtle.pensize(10)
        self.turtle.shapesize(0.1, 0.1, 1)
        self.turtle.speed("fastest")

        for dot_count in range(1, x_count * y_count + 1):
            color = choice(self.extracted_colors) if len(self.extracted_colors) == 0 else random_rgb_color()
            self.draw_dot(color)

            if dot_count % x_count == 0:
                self.turtle.setheading(90)
                self.turtle.penup()  # Lift the pen
                self.turtle.forward(DISTANCE_BETWEEN_SPOTS)
                self.turtle.setheading(180)
                self.turtle.forward(DISTANCE_BETWEEN_SPOTS * x_count)
                self.turtle.setheading(0)
                self.turtle.pendown()  # Lower the pen

    def move_forward(self):
        self.turtle.forward(10)

    def move_backward(self):
        self.turtle.backward(10)

    def turn_left(self):
        self.turtle.setheading(self.turtle.heading() + 10)

    def turn_right(self):
        self.turtle.setheading(self.turtle.heading() - 10)

    def clear_drawing(self):
        self.turtle.clear()
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()
