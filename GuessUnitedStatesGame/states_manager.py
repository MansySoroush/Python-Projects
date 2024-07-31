import pandas
from turtle import Turtle

FONT = ("Courier", 10, "bold")

MAX_STATES = 50


class StatesManager:
    def __init__(self):
        self.score = 0
        self.total_states = MAX_STATES
        self.guessed_states = []
        self.writer = Turtle("circle")
        self.writer.shapesize(0.1, 0.1, 1)
        self.writer.penup()
        self.writer.speed("fastest")
        self.writer.color("blue")
        # self.writer.hideturtle()

    def check_state_validity(self, state_name):
        data = pandas.read_csv("50_states.csv")
        state_row = data[data["state"] == f"{state_name}"]
        if state_row["state"].count() == 1:
            self.score += 1
            self.guessed_states.append(state_name)
            x_pos = state_row["x"].values[0]
            y_pos = state_row["y"].values[0]
            self.write_state(state_name, x_pos, y_pos)
            return True
        return False

    def check_state_validity2(self, state_name):
        data = pandas.read_csv("50_states.csv")
        all_states = data.state.to_list()
        if state_name in all_states:
            self.score += 1
            self.guessed_states.append(state_name)
            state_data = data[data.state == state_name]
            self.write_state(state_name, int(state_data.x), int(state_data.y))
            return True
        return False

    def write_state(self, state_name, x_pos, y_pos):
        self.writer.goto(x_pos, y_pos)
        self.writer.write(state_name, align="center", font=FONT)

    def terminate(self):
        data = pandas.read_csv("50_states.csv")
        all_states = data.state.to_list()

        missing_states = [state for state in all_states if state not in self.guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in self.guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")

