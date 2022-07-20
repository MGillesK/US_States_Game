import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the state name?").title()

    data = pandas.read_csv("50_states.csv")
    list_states = data.state.to_list()
    list_x = data.x.to_list()
    list_y = data.y.to_list()

    if answer_state == "Exit":
        states_to_learn = [state for state in list_states if state not in guessed_states]

        break

    if answer_state in list_states:
        guessed_states.append(answer_state)
        index = list_states.index(answer_state)
        label = turtle.Turtle()
        label.penup()
        label.goto(list_x[index], list_y[index])
        label.write(answer_state)

# states_to_learn = []
# for state in list_states:
#     if state not in guessed_states:
#         states_to_learn.append(state)


data = pandas.DataFrame(states_to_learn)
data.to_csv("missed_states.csv")

screen.exitonclick()
