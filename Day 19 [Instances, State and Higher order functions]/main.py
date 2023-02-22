import random
from turtle import Turtle, Screen

# etch a sketch game


# tim = Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_clockwise():
#     angle = tim.heading()
#     angle -= 10
#     tim.setheading(angle)
#
#
# def move_counter_clockwise():
#     angle = tim.heading()
#     angle += 10
#     tim.setheading(angle)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["blue", "yellow", "black", "green", "orange", "purple"]
y_pos = -150

all_turtle = []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(color[i])
    tim.penup()
    tim.goto(x=-230, y=y_pos)
    y_pos += 50
    all_turtle.append(tim)
tim.speed(300)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winning color")
            else:
                print(f"You've lost! The {winning_color} turtle is the winning color")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
