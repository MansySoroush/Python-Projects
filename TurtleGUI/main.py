from turtle import Screen, Turtle
import TurtleRace
from Painter import PaintManager

screen = Screen()
screen.colormode(255)
screen.setup(width=TurtleRace.PLAY_GROUND_WIDTH, height=TurtleRace.PLAY_GROUND_HEIGHT)

user_bet_color = screen.textinput(title="Make your bet", prompt="Which color will win the race? Enter a color: ")
turtle_race = TurtleRace.TurtleRacePlay(turtle_count=10, user_color=user_bet_color)

if user_bet_color != "":
    winner_color = turtle_race.start_game()
    if winner_color.lower() == user_bet_color.lower():
        print(f"You've won! The {winner_color} turtle is the winner!")
    else:
        print(f"You've lost! The {winner_color} turtle is the winner!")

# turtle = Turtle()
# painter = PaintManager(turtle)


# painter.draw_dashed_line(150, 10)
# painter.draw_complex_shape(13)
# painter.draw_random_walk()
# painter.draw_spiro_graph(5)

# painter.extract_colors_from_image("image.jpg", 30)
# painter.draw_spots(10, 10)

# screen.listen()
# screen.onkey(key="w", fun=painter.move_forward)
# screen.onkey(key="s", fun=painter.move_backward)
# screen.onkey(key="a", fun=painter.turn_left)
# screen.onkey(key="d", fun=painter.turn_right)
# screen.onkey(key="c", fun=painter.clear_drawing)

screen.exitonclick()
