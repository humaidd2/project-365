import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.tolist()
score = 0
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="Type another state name: ").title()

    if answer_state.title() == "Exit":
        states_to_learn = [state for state in state_list if state not in guessed_state]

        to_learn_dict = {
            "state": states_to_learn
        }
        to_learn = pandas.DataFrame(to_learn_dict)
        to_learn.to_csv("states_to_learn")
        break
    if answer_state in state_list:
        w = turtle.Turtle()
        w.hideturtle()
        w.color("black")
        w.penup()
        state_data = data[data.state == answer_state]
        w.goto(int(state_data.x), int(state_data.y))
        w.write(f"{answer_state}", font=("Arial", 10, "normal"))
        guessed_state.append(answer_state)
        score += 1



turtle.mainloop()
