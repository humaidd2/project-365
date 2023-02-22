import random
import turtle
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
turtle.colormode(255)
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")
direction = [90, 180, 270, 360]
timmy_the_turtle.speed(200)
r_color = ["red", "yellow", "green", "orange"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

a = 0
while a < 360:
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.setheading(a)
    timmy_the_turtle.circle(100)
    a += 5

screen = Screen()
screen.exitonclick()
