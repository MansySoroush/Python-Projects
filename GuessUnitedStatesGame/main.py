import turtle
from states_manager import StatesManager, MAX_STATES

screen = turtle.Screen()
screen.title("US. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# # To Collect the coordinates corresponded to each state on the map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

state_manager = StatesManager()


game_is_on = True
while game_is_on:
    user_answer = screen.textinput(f"{state_manager.score}/50 Guess the US. State",
                                   "What's another state's name?").title()
    if user_answer == "Exit":
        break

    if user_answer is not None:
        if state_manager.check_state_validity(user_answer):
            game_is_on = (state_manager.score < MAX_STATES)
    else:
        game_is_on = False

state_manager.terminate()
