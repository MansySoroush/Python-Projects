from turtle import Turtle, TurtleScreen
from data import game_colors, game_status, player_names
from random import choice, randint

PLAY_GROUND_WIDTH = 500
PLAY_GROUND_HEIGHT = 500
PLAY_GROUND_LEFT_MARGIN = 50
PLAY_GROUND_RIGHT_MARGIN = 50
VERTICAL_TURTLES_DISTANCE = 40
PLAY_GROUND_START_LEFT_POS = -1 * (PLAY_GROUND_WIDTH / 2) + PLAY_GROUND_LEFT_MARGIN
PLAY_GROUND_START_RIGHT_POS = PLAY_GROUND_WIDTH / 2 - PLAY_GROUND_LEFT_MARGIN
PLAY_GROUND_FINAL_BAR_POS = PLAY_GROUND_START_RIGHT_POS
MAX_PLAYER_COUNT = 15


# All turtles by default have a height of 20px and width of 20px.

class TurtleRacePlay:
    def __init__(self, turtle_count, user_color):
        self.colors = []
        self.turtles = []
        self.result = []
        self.turtle_names = []
        self.final_wall_pos = 0
        self.player_count = turtle_count if turtle_count < MAX_PLAYER_COUNT else MAX_PLAYER_COUNT
        self.user_color = user_color
        self.game_turtle = Turtle()
        self.screen = self.game_turtle.getscreen()

        self.init_main_turtle()
        self.add_players()
        self.draw_final_wall()

    def add_players(self):
        for n in range(0, self.player_count):
            if n == 0:
                color = self.user_color
            else:
                color = self.get_uniq_color()
            self.colors.append(color)

        start_x_pos = PLAY_GROUND_START_LEFT_POS
        start_y_pos = self.get_bottom_race_area()

        for n in range(0, self.player_count):
            turtle_color = choice(self.colors)
            self.colors.remove(turtle_color)

            self.add_player(n, turtle_color, start_x_pos, start_y_pos)
            start_y_pos += VERTICAL_TURTLES_DISTANCE

    def add_player(self, index, color, x_pos, y_pos):
        t = Turtle("turtle")
        t.color(color)
        # t.hideturtle()
        t.penup()
        t.goto(x_pos, y_pos)
        t.pendown()
        # t.showturtle()

        self.write_label(index, t)
        self.turtles.append(t)

    def get_uniq_color(self):
        color_name = choice(game_colors)
        while self.colors.__contains__(color_name):
            color_name = choice(game_colors)
        return color_name

    def get_race_area_height(self):
        return (self.player_count - 1) * VERTICAL_TURTLES_DISTANCE

    def get_bottom_race_area(self):
        race_area_height = self.get_race_area_height()
        start_y_pos = -1 * (race_area_height / 2)
        return start_y_pos

    def init_result(self):
        self.result.clear()
        for _ in range(0, self.player_count):
            self.result.append(game_status["Start"])

    def init_main_turtle(self):
        self.game_turtle.hideturtle()
        self.game_turtle.penup()
        self.game_turtle.shape("circle")
        self.game_turtle.shapesize(0.1, 0.1, 1)
        self.game_turtle.speed("fastest")

    def draw_final_wall(self):
        start_x_pos = PLAY_GROUND_FINAL_BAR_POS
        offset = 10
        start_y_pos = self.get_bottom_race_area() - offset

        self.game_turtle.goto(x=start_x_pos, y=start_y_pos)
        self.game_turtle.pensize(2)
        self.game_turtle.showturtle()
        self.game_turtle.pendown()

        race_area_height = self.get_race_area_height()
        self.game_turtle.color("black")
        self.game_turtle.setheading(90)
        self.game_turtle.forward(race_area_height + 2 * offset)
        self.game_turtle.hideturtle()
        self.game_turtle.penup()

    def write_label(self, index, turtle):
        turtle_x_pos = turtle.pos()[0]
        turtle_y_pos = turtle.pos()[1] - 3
        turtle_color = turtle.pencolor()

        label_font = ("Arial", 12, "bold")

        label = player_names[index] if turtle_color != self.user_color else "You"
        label_x_pos = turtle_x_pos - PLAY_GROUND_LEFT_MARGIN + 20
        label_y_pos = turtle_y_pos - 5

        self.game_turtle.goto(x=label_x_pos, y=label_y_pos)
        self.game_turtle.color(turtle_color)
        self.game_turtle.showturtle()
        self.game_turtle.pendown()
        self.game_turtle.write(label, align="center", font=label_font)
        self.game_turtle.hideturtle()
        self.game_turtle.penup()

    def is_still_in_progress(self):
        for n in range(0, self.player_count):
            if self.result[n] == game_status["In Progress"]:
                return True
        return False

    def start_game(self):
        is_race_on = True
        self.init_result()

        winner_index = -1
        while is_race_on:
            turtle_index = randint(0, self.player_count - 1)
            turtle_status = self.result[turtle_index]

            if turtle_status != game_status["Win"] and turtle_status != game_status["Lose"]:
                t = self.turtles[turtle_index]

                step_forward = randint(0, 10)
                t.penup()
                t.forward(step_forward)

                current_turtle_pos = t.pos()
                if current_turtle_pos[0] >= PLAY_GROUND_FINAL_BAR_POS:
                    if winner_index == -1:
                        self.result[turtle_index] = game_status["Win"]
                        winner_index = turtle_index
                    else:
                        self.result[turtle_index] = game_status["Lose"]
                else:
                    self.result[turtle_index] = game_status["In Progress"]

            is_race_on = self.is_still_in_progress()

        winner_turtle = self.turtles[winner_index]
        winner_color = winner_turtle.pencolor()
        return winner_color
