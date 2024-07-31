import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=player.move_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_cars()

    # To detect collision with cars
    game_is_on = not car_manager.is_collided(player)

    # To detect successful crossing
    if game_is_on:
        if player.is_successful_crossed():
            player.restart()
            car_manager.level_up()
            score_board.level_up()
    else:
        score_board.game_over()

screen.exitonclick()
