from state_name import StateName
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

the_states_list = pandas.read_csv("50_states.csv")
states = the_states_list.state
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's a U.S. state's name? ").title()
    for sta in states:
        if answer_state == sta:
            state_x = int(the_states_list[the_states_list.state == sta].x)
            state_y = int(the_states_list[the_states_list.state == sta].y)
            new_state = StateName()
            new_state.write_the_state(s_name=sta, x=state_x, y=state_y)
            guessed_states.append(sta)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()


